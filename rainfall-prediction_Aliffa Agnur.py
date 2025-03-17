import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import copy
import shap
#import optuna
import keras_tuner as kt
import statsmodels.stats.multitest as smm
from scipy import stats
from scipy.stats.mstats import winsorize
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split , KFold, cross_val_score
from sklearn.preprocessing import RobustScaler, StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from imblearn.over_sampling import SMOTE, BorderlineSMOTE, ADASYN, SVMSMOTE
from sklearn.metrics import roc_auc_score, auc, roc_curve , accuracy_score, confusion_matrix , matthews_corrcoef
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.tree import DecisionTreeClassifier

#import lightgbm
#import xgboost as xgb
#import catboost


# SEED

import random

seed_value = 2024

random.seed(seed_value)
np.random.seed(seed_value)
tf.random.set_seed(seed_value)

train_data = pd.read_csv(r'https://raw.githubusercontent.com/BapakmuLah/Rainfall-Prediction_Dicoding/refs/heads/main/data/train.csv')
test_data  = pd.read_csv(r'https://raw.githubusercontent.com/BapakmuLah/Rainfall-Prediction_Dicoding/refs/heads/main/data/test.csv')

# ----------------------------------------------------------------------------------------------------------

# FEATURE ENGINEERING


# HANDLING MISSING VALUES

# REPLACE NULL VALUES WITH MEDIAN
test_data['winddirection'] = test_data['winddirection'].fillna(value= test_data['winddirection'].median())  

test_data['winddirection'].isna().sum()

# ----------------------------------------------------------------------------------------------------------

# FEATURE ENGINEERING . CREATE NEW FEATURE

combined_data = pd.concat((train_data, test_data))  # MERGE TRAIN AND TEST DATA


combined_data['temp_range'] = combined_data['maxtemp'] - combined_data['mintemp']

# TO REFLECT THE RELATIVE HUMIDITY OF THE AIR
combined_data['temp_dew_spread'] = combined_data['temparature'] - combined_data['dewpoint']

'''combines temperature, dew point, and humidity to measure the “felt” temperature. High values ​​indicate hot, humid conditions, 
   which are often associated with the potential for convective precipitation.''' 
combined_data['heat_index'] = 0.5 * (combined_data['temparature'] + combined_data['dewpoint']) + 0.1 * combined_data['humidity'] - 10

# CREATE A NEW DIRECTION FEATURE SO THAT THE MODEL UNDERSTANDS 'WINNDDIRECTION' PATTERNS
combined_data['wind_east'] = combined_data['windspeed'] * np.cos(combined_data['winddirection'])
combined_data['wind_north']= combined_data['windspeed'] * np.sin(combined_data['winddirection'])

# INTERACTION BETWEEN HUMIDITY AND CLOUD
combined_data['humidity_cloud'] = combined_data['humidity'] * combined_data['cloud']

# THIS FEATURE MEASURES THE RATIO OF HOW MUCH SUN LIGHT IS BLOCKED BY CLOUDS
combined_data['sunshine_cloud_ratio'] = combined_data['sunshine'] / (combined_data['cloud'] + 1e-5)

# THE COMBINATION OF DEWPOINT AND HUMIDITY REFLECTS THE WATER VAPOR CONTENT IN THE AIR
combined_data['moisture_index'] = combined_data['dewpoint'] * combined_data['humidity']

# DESCRIBING THE TEMPERATURE FELT DUE TO THE COMBINATION OF TEMPERATURE AND WIND
combined_data['wind_chill'] = 13.12 + 0.6215 * combined_data['temparature'] - 11.37 * (combined_data['windspeed']**0.16) + 0.3965 * combined_data['temparature'] * (combined_data['windspeed']**0.16)  


def set_high_rain(row):
   if row['humidity'] > 80 and row['cloud'] > 80:
      return 1
   else:
      return 0

combined_data['high_rain_risk'] = combined_data.apply(set_high_rain, axis=1)



# RE-SEPARATE TRAIN AND TEST DATA
TRAIN_SIZE = 2190
new_train_data = combined_data[:TRAIN_SIZE]
new_test_data  = combined_data[TRAIN_SIZE:]

# --------------------------------------------------------------------------------------------------

# WINSORIZATION

new_train_data['sunshine_cloud_ratio'] = winsorize(a = new_train_data['sunshine_cloud_ratio'], limits=[0, 0.01])
new_test_data['sunshine_cloud_ratio'] = winsorize(a = new_test_data['sunshine_cloud_ratio'], limits=[0, 0.01])


# ------------------------------------------------------------------------------------------------------

# SPLIT DATASET

x = new_train_data.drop(labels=['id', 'rainfall'], axis=1)
y = new_train_data['rainfall']

x_train, x_val, y_train, y_val = train_test_split(x,y, test_size=0.20, random_state= 2025, shuffle=True)

print(f'Type : {type(x_train)}')
print(f'x_train shape : {x_train.shape}')
print(f'x_test shape  : {x_val.shape}')
print(f'y_train shape : {y_train.shape}')
print(f'y_test shape  : {y_val.shape}')


# ----------------------------------------------------------------------------------------------------

# FEATURE SCALING

cols_to_robust = ['pressure', 'dewpoint', 'humidity', 'cloud', 'windspeed', 'temp_range', 'temp_dew_spread', 'humidity_cloud', 'sunshine_cloud_ratio', 'moisture_index']
cols_to_zscore = ['day','maxtemp','temparature','mintemp','sunshine','winddirection', 'heat_index', 'wind_east', 'wind_north', 'wind_chill']

# DEFINE NORMALIZATION TECHNIQUE
robust = RobustScaler()
zscore = StandardScaler()

# FIT AND TRANSFORM TRAIN DATA
x_train[cols_to_robust] = robust.fit_transform(x_train[cols_to_robust])
x_train[cols_to_zscore] = zscore.fit_transform(x_train[cols_to_zscore])

# TRANSFORM VALIDATION DATA
x_val[cols_to_robust] = robust.transform(x_val[cols_to_robust])
x_val[cols_to_zscore] = zscore.transform(x_val[cols_to_zscore])

# TRANSFORM TEST DATA
#new_test_data = copy.deepcopy(test_data)
new_test_data[cols_to_robust] = robust.transform(new_test_data[cols_to_robust])
new_test_data[cols_to_zscore] = zscore.transform(new_test_data[cols_to_zscore])


# -----------------------------------------------------------------------------------------------------------

# SVM SMOTE
svm_smote = SVMSMOTE(sampling_strategy=0.45, random_state= seed_value, m_neighbors = 3, k_neighbors=4)
x_resampled, y_resampled = svm_smote.fit_resample(x_train, y_train)


# -------------------------------------------------------------------------------------------------------------------------------------

# MODEL DEVELOPMENT 


# BUILD FEEDFORWARD ARCHITECTURE WITH KERAS-TUNER

def build_model(hp):
    model = tf.keras.Sequential()

    # DEFINE INPUT LAYER
    model.add(tf.keras.layers.Input(shape= (x_train.shape[1],)))

    # FIRST HIDDEN LAYERS
    model.add(tf.keras.layers.Dense(units= hp.Int( name = 'hidden_layer_1', min_value= 150, max_value = 300, step= 15 ), 
                                    activation='relu', 
                                    kernel_initializer='HeNormal',
                                    kernel_regularizer= tf.keras.regularizers.L2( hp.Float(name= 'L2_Regularizer', 
                                                                                           min_value = 0.001, 
                                                                                           max_value= 0.015, 
                                                                                           default= 0.005))))
    
    # CREATE 1 - 3 MORE HIDDEN LAYERS (KERAS-TUNER WILL CHOOSE THE BEST COMBINATION)
    for i in range(hp.Int(name= 'num_layers', min_value = 1, max_value = 3)):
        
        model.add(tf.keras.layers.Dense(units= hp.Int( name = 'hidden_layer_' + str(i + 1), 
                                                      min_value = 35, 
                                                      max_value=200, 
                                                      step = 15 ),
                                                      
                                        activation='relu', 
                                        kernel_initializer='HeNormal'))
        # DROPOUT LAYERS
        model.add(tf.keras.layers.Dropout(rate= hp.Float( name = 'dropout_' + str(i+1), min_value=0.35, max_value=0.6, step=0.07)))
        

    # OUTPUT LAYERS
    model.add(tf.keras.layers.Dense(units=1, activation='sigmoid', kernel_initializer='glorot_normal'))

    # DEFINE COMPILER
    model.compile(optimizer= 'adam', loss='binary_crossentropy', metrics=[tf.keras.metrics.AUC()])

    return model


# DEFINE TUNER
tuner = kt.RandomSearch(hypermodel= build_model, 
                        objective= kt.Objective('val_auc', direction='max'), 
                        max_trials= 15, 
                        seed= 2025, 
                        tune_new_entries= True, 
                        allow_new_entries= True, 
                        max_retries_per_trial= 3, 
                        max_consecutive_failed_trials=2,
                        overwrite=True)

# DEFINE CALLBACKS
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_auc', patience=24, verbose=0, restore_best_weights=True) 
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_auc', patience=10, verbose=1, min_lr= 0.000001, factor=0.4)

# SEARCH ALL COMBINATION BEST HYPERATAMETERS
tuner.search(x_train, y_train, batch_size= 32, epochs=100, validation_data= (x_val, y_val), callbacks=[reduce_lr, early_stopping])


# ---------------------------------------------------------------------------------------------------------------------------------

# EVALUATION

# TAKE BEST MODEL
best_model = tuner.get_best_models(num_models=1)[0]

# PREDICT
y_pred_prob = best_model.predict(x_val)

# CALCULATE ROC AUC SCORE
roc_auc = roc_auc_score(y_val, y_pred_prob)
print(f'ROC AUC Score: {roc_auc}')


# SAVE MODEL
best_model.save('Rainfall-Prediction_Keras-Tuner.h5')

# EVALUATION VALIDATION DATA

y_pred = best_model.predict(x_val)

# COMPUTE ROC_CURVE
fpr, tpr, threshold = roc_curve(y_val, y_pred)

# COMPUTE AUC
roc_auc_score = auc(x= fpr, y= tpr)

# PLOT ROC CURVE
plt.figure(figsize=(10,5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Roc-Auc curve : {roc_auc_score:.2f}')
plt.plot([0,1],[0,1], color='red', lw=2, linestyle='--')    # RANDOM LINE (Random Classification)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC-AUC Curve')
plt.legend()



# DISPLAY DISTRIBUTION PROBABILITY PREDICTION

plt.figure(figsize=(15,5))

# DISPLAY PROBABILITY PREDICTED
plt.subplot(1,2,1)
sns.histplot(y_pred, bins=10, color='lightblue', legend=False)
plt.xlabel('Distribution Probability')
plt.ylabel('Frequency')
plt.title('Prediction Probability Distribution')

# DISPLAY RAINFALL CLASS DISTRIBUTION AT VALIDATION DATA
plt.subplot(1,2,2)
sns.countplot(x = y_val, color='skyblue')
plt.xticks(ticks=[0, 1], labels=['No Rain', 'Rain'])
plt.title('Rainfall Class Distribution')
plt.show()




# SHOWING PROBABILITY DISTRIBUTIONS FOR TP, FP, FN, TN

y_preds = y_pred.flatten()   # CONVERT T0 1D ARRAY

# CALCULATE TP, FP, FN, TN
TP = (y_val == 1) & (y_preds >= 0.5)
FP = (y_val == 0) & (y_preds >= 0.5) 
FN = (y_val == 1) & (y_preds < 0.5)   
TN = (y_val == 0) & (y_preds < 0.5)   

total_data = len(y_val)
FP_percentage = len(FP) / total_data * 100
FN_percentage = len(FN) / total_data * 100

# DISPLAY HISTPLOT
plt.figure(figsize=(10,7))

plt.subplot(2,2,1)
sns.histplot(y_preds[TP], bins=5, legend=False, color='skyblue')
plt.xlabel('Probability')
plt.ylabel('Frequency')
plt.title('True Positive  (True = Rain, Predicted = Rain)')

plt.subplot(2,2,2)
sns.histplot(y_preds[FP], bins=5, legend=False, color='skyblue')
plt.xlabel('Probability')
plt.ylabel('Frequency')
plt.title('False Positive  (True = No Rain, Predicted= Rain)')

plt.subplot(2,2,3)
sns.histplot(y_preds[FN], bins=5, legend=False, color='skyblue')
plt.xlabel('Probability')
plt.ylabel('Frequency')
plt.title('False Negative  (True= Rain, Predicted= No Rain)')

plt.subplot(2,2,4)
sns.histplot(y_preds[TN], bins=5, legend=False, color='skyblue')
plt.xlabel('Probability')
plt.ylabel('Frequency')
plt.title('True Negative  (True = No Rain, Predicted= No Rain)')

plt.tight_layout()



# CHECK FEATURE IMPORTANCES USING SHAP


# DEFINE SHAP
masker = shap.maskers.Independent(x_train)
explainer = shap.Explainer(best_model, masker)

shap_values = explainer.shap_values(x_val)


plt.title("Feature Importance Analysis for Rainfall Prediction", fontsize=14)

# PLOT SHAP
shap.summary_plot(shap_values, x_val, feature_names= x_train.columns.tolist())



