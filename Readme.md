# Laporan Proyek Machine Learning - Aliffa Agnur

## Domain Proyek

Hujan merupakan salah satu fenomena alam yang menunjukan jatuhnya titik air dari atmosfer ke permukaan bumi. Curah hujan adalah jumlah air yang jatuh di tanah datar selama periode tertentu yang diukur dengan satuan tinggi (mm) di atas permukaan horizontal. Jumlah curah hujan diukur sebagai volume air yang jatuh di atas permukaan bidang datar dalam periode waktu tertentu, yaitu harian, mingguan, bulanan, atau tahunan. Intensitas curah hujan yang tinggi yang sering disebut hujan ekstrem dapat mengakibatkan terjadinya bencana alam (Laia & Setyawan, 2020). [[1]](https://eprints.unpak.ac.id/7983/1/Skripsi_065119023_Feri%20Irawan.pdf) <br>
Curah hujan yang tidak menentu dapat menyebabkan banjir, kekeringan, dan kerugian ekonomi. Oleh karena itu, prediksi curah hujan yang akurat sangat penting untuk perencanaan dan pengambilan keputusan yang efektif. [[2]](https://ejurnal.itenas.ac.id/index.php/mindjournal/article/view/9220) <br>
Curah hujan dapat diprediksi dengan menerapkanMachine Learning yang merupakan cabang ilmu turunan dari Artificial Intelligenceatau kecerdasan buatan. Machine Learning membahas bagaimana algoritma komputer dapat mempelajari data yang diinputkan dengan mengenali sifat karakter data atau pola data, kemudian akan mengubah pola data yang berhasil dipelajari menjadi sebuah tindakan yang meminimalisir pekerjaan yang membutuhkan manusia. [[3]](https://repository.unsri.ac.id/83938/3/RAMA_45201_08021381823054_0015096101_0009067603_01_front_ref.pdf) <br>

**Mengapa Masalah ini harus diselesaikan?**:
1.  Prediksi curah hujan yang akurat sangat penting dalam sektor pertanian, karena membantu petani merencanakan waktu tanam dan panen dengan lebih efisien, sehingga dapat meningkatkan hasil pertanian dan mengurangi risiko gagal panen. [Pentingnya Memahami Cuaca dan Pengaruhnya ke Pertanian](https://ugm.ac.id/id/berita/pentingnya-memahami-cuaca-dan-pengaruhnya-ke-pertanian/) <br>
2. Dalam perencanaan kota, data curah hujan yang akurat memungkinkan pemerintah dan perencana kota mengelola infrastruktur perkotaan, seperti sistem drainase, untuk mencegah banjir dan kerusakan lainnya. [Pentingnya Sensor Curah Hujan pada Weather Station](https://loggerindo.com/2024/11/14/pentingnya-sensor-curah-hujan-pada-weather-station/) <br>
3. Curah hujan memiliki peran terpenting dalam menentukan ketersediaan air di berbagai wilayah. Ketika air hujan turun, maka sebagian air akan mengalir di permukaan tanah sebagai limpasan, mengisi waduk, danau, sungai, sedangkan sebagian lainnya meresap ke dalam tanah untuk memperbarui akuifer. Tersedianya curah hujan yang cukup sangat penting untuk menjamin ketersediaan air bagi berbagai kebutuhan manusia, dimulai dari kebutuhan rumah tangga, operasional industri, hingga irigasi pertanian. [Pemantauan Curah Hujan untuk Manajemen Sumber Daya Air yang Berkelanjutan](https://www.mertani.co.id/post/pemantauan-curah-hujan-untuk-manajemen-sumber-daya-air-yang-berkelanjutan)


**Bagaimana Masalah ini diselesaikan?** :
1. <a href="https://scholar.google.com/citations?view_op=view_citation&hl=id&user=8mExcgIAAAAJ&citation_for_view=8mExcgIAAAAJ:KlAtU1dfN6UC" style="text-decoration: none;">Prediksi Curah Hujan Harian di Stasiun Meteorologi Kemayoran Menggunakan Artificial Neural Network (ANN)</a>

   - Penelitian ini memanfaatkan jaringan saraf tiruan untuk memprediksi curah hujan harian di Stasiun Meteorologi Kemayoran. Data cuaca harian dari Januari 2011 hingga Desember 2019 digunakan untuk pelatihan model, yang kemudian diuji dengan data dari Januari hingga Agustus 2020. Variasi model dibuat berdasarkan jenis input dan jumlah lapisan tersembunyi. Hasil penelitian menunjukkan bahwa penggunaan parameter input kondisi cuaca permukaan seperti suhu udara, kelembaban udara, dan durasi penyinaran matahari memberikan nilai koefisien korelasi sebesar 0,4–0,5 dan MAE 9,7–9,8 mm. Sebaliknya, penggunaan data hujan hari-hari sebelumnya sebagai input menghasilkan korelasi 0,1–0,3 dan MAE 11,3–12,3 mm, menunjukkan bahwa parameter cuaca permukaan lebih efektif sebagai prediktor.

2. [Prediksi Curah Hujan di Wilayah DKI Jakarta dengan Model NeuralProphet](https://scholar.google.com/citations?view_op=view_citation&hl=id&user=8Z4345gAAAAJ&citation_for_view=8Z4345gAAAAJ:2P1L_qKh6hAC)
   - Penelitian ini menggunakan model NeuralProphet untuk memprediksi curah hujan bulanan dan harian di DKI Jakarta. Data yang digunakan adalah data satelit PERSIAN-CCS dari Januari 2005 hingga Juni 2021. Hasil penelitian menunjukkan bahwa secara spasial, model NeuralProphet dapat mengklasifikasikan persebaran curah hujan di wilayah DKI Jakarta. Namun, terdapat perbedaan nilai yang cukup tinggi antara prediksi dan data observasi. Prediksi bulanan menghasilkan akurasi terbaik dengan korelasi 0,8, RMSE 58,45 mm, dan MAE 23,37 mm, sedangkan prediksi harian memiliki korelasi 0,55, RMSE 10,73 mm, dan MAE 9,32 mm.

3. <a href="https://journal.universitasmulia.ac.id/index.php/seminastika/article/view/237" style="text-decoration: none;">PREDIKSI TINGGI CURAH HUJAN DAN KECEPATAN ANGIN BERDASARKAN DATA CUACA DENGAN PENERAPAN ALGORITMA ARTIFICIAL NEURAL NETWORK (ANN)</a>
   - Berdasarkan hasil yang telah diperoleh selama   proses   pengerjaan   yaitu   melakukan prediksi  terhadap  curah  hujan  dan  kecepatan angin     maka     dapat     disimpulkan     bahwa pemodelan  terbaik  dalam  melakukan  prediksi curah hujan adalah dengan algoritma Backprpagation  Neural  Network yaitu  dengan dengan  nilai  RMSE  0.079535  yaitu  dengan  20 neuron,  1000 epoch, serta validation  split 0.1. Untuk   pemodelan   terbaik   dalam   melakukan prediksi    kecepatan    angin    adalah    dengan menggunakan    algoritma Reccurent    Neural Network dengan  menggunakan  arsitektur Long Short Term Memory (LSTM) yaitu dengan nilai RMSE   yang   diperoleh   berada   pada   nilai 0.06281251 dengan 30 neuron, 800 epoch, serta validation split 0.1. 


## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

1. Bagaimana cara membangun model yang dapat mengklasifikasikan kejadian hujan berdasarkan fitur-fitur yg ada di dataset tsb?
2. Fitur mana saja yang memiliki korelasi signifikan dan berpengaruh dalam prediksi klasifikasi hujan? Sejauh mana masing-masing fitur mempengaruhi hasil prediksi?
3. Bagaimana mengatasi ketidakseimbangan kelas pada data target agar model dapat belajar dengan baik dari setiap kelas dan meningkatkan akurasi prediksi, terutama pada kelas minoritas?

### Goals

1. Membangun model prediksi yang mampu mengklasifikasikan kejadian hujan dengan akurasi tinggi menggunakan metrik evaluasi ROC-AUC. Metrik ROC-AUC sangat berguna dalam mengukur performa model klasifikasi, khususnya dalam situasi imbalanced data, karena metrik ini mempertimbangkan trade-off antara True Positive Rate dan False Positive Rate.
2. Melakukan analisis mendalam terhadap korelasi antar fitur untuk mengidentifikasi fitur-fitur utama yang berpengaruh dalam prediksi hujan. Hal ini juga mendukung upaya feature engineering untuk menghasilkan pola baru yang lebih representatif dari data asli.
3. Menerapkan teknik oversampling, seperti SMOTE, borderline SMOTE, ADASYN, dan SVM SMOTE, guna menangani permasalahan ketidakseimbangan kelas. Dengan demikian, model dapat memperoleh pembelajaran yang lebih seimbang dan meningkatkan performa evaluasi menggunakan ROC-AUC.

    ### Solution statements
   1. **Membangun Ensemble Model dengan Algoritma Boosting dan Menggabungkan nya menggunakan Fusion Model**
      - Menerapkan beberapa algoritma boosting seperti GBM, LGBM, AdaBoost, XGBoost, dan CatBoost.
      - Mengoptimasi hyperparameter masing-masing model menggunakan Optuna.
      - Menggabungkan model-model tersebut melalui teknik Stacking untuk meningkatkan kekuatan prediksi dan mengurangi risiko overfitting.
   2. **Menggunakan Keras-Tuner untuk membangun Model Prediksi**
      - Membangun model deep learning Menggunakan FeedForward Neural Network Architecture.
      - Menggunakan Keras-Tuner untuk menemukan kombinasi hyperparameter terbaik sehingga model dapat belajar dengan optimal dari data.
   3. **Feature Engineering**
      - Menerapkan teknik feature engineering untuk menciptakan fitur baru yang dapat menangkap pola tersembunyi dari data asli.
      - Analisis korelasi akan membantu dalam pemilihan fitur yang relevan sehingga model menjadi lebih efisien dan akurat.
   4. **Penanganan Imbalanced Data**
      - Mengimplementasikan berbagai teknik oversampling (SMOTE, borderline SMOTE, ADASYN, SVM SMOTE) untuk menyeimbangkan distribusi kelas dalam data target.
      - Teknik ini diharapkan dapat meningkatkan kemampuan model dalam mempelajari karakteristik masing-masing kelas, terutama kelas yang kurang terwakili.

## Data Understanding
Dataset ini merupakan kumpulan data meteorologi yang disusun untuk tujuan prediksi curah hujan melalui pendekatan klasifikasi. Data diambil dalam satuan waktu tertentu (misalnya harian) dan memuat berbagai fitur yang berkaitan dengan kondisi cuaca. Tujuan dataset ini untuk memprediksi hujan berdasarkan fitur-fitur yg tersedia. 
Dataset ini bisa diakses di : [Binary Prediction with a Rainfall Dataset](https://www.kaggle.com/competitions/playground-series-s5e3/overview/timeline)

### Variabel-variabel pada Rainfall Prediction Dataset adalah sebagai berikut:

| **Nama Fitur**     | **Penjelasan**                                                                                       |
|--------------------|------------------------------------------------------------------------------------------------------|
| `id`               | Identifier unik untuk setiap entri data.                                                             |
| `day`              | Mewakili hari pengamatan. day 1 - 365                                                                |
| `pressure`         | Nilai tekanan udara yang berpengaruh pada kondisi atmosfer. (hPa).                                   |
| `maxtemp`          | Suhu maksimum (°C) pada hari tersebut.                                                               |
| `temparature`      | Suhu rata-rata (°C) sepanjang hari.                                                                  |
| `mintemp`          | Suhu minimum (°C) pada hari tersebut.                                                                |
| `dewpoint`         | Titik embun (°C).                                                                                    |
| `humidity`         | Kelembapan relatif (%).                                                                              |
| `cloud`            | Persentase tutupan awan (%). Tutupan awan yang tinggi sering dikaitkan dengan potensi hujan.         |
| `sunshine`         | Jumlah sinar matahari (jam). Semakin sedikit sinar matahari, peluang hujan biasanya meningkat.       |
| `winddirection`    | Arah angin (derajat). Memengaruhi pola cuaca dengan membawa kelembapan dari wilayah tertentu.        |
| `windspeed`        | Kecepatan angin (km/jam). Indikasi keberadaan sistem cuaca yang kuat yang bisa menghasilkan hujan.   |
| `rainfall`         | Prediksi Hujan (0 = Tidak Hujan, 1 = Hujan)                                                          |



## Exploratory Data Analysis (EDA)
Analisis ini menggunakan 2 File CSV yg berbeda , yaitu :
  1. **train.csv** : digunakan untuk membuat model prediksi dan mengevaluasinya. terdiri dari 2190 baris dan 13 kolom.
  2. **test.csv**  : digunakan untuk memprediksi model berdasarkan data baru yg belum pernah ada sebelumnya. terdiri dari 730 baris dan 13 kolom.

### Isi Dataset 
| id | day | pressure | maxtemp | temparature | mintemp | dewpoint | humidity | cloud | sunshine | winddirection | windspeed | rainfall |
|----|-----|----------|---------|-------------|---------|----------|----------|-------|----------|---------------|-----------|----------|
| 0  | 1   | 1017.4   | 21.2    | 20.6        | 19.9    | 19.4     | 87.0     | 88.0  | 1.1      | 60.0          | 17.2      | 1        |
| 1  | 2   | 1019.5   | 16.2    | 16.9        | 15.8    | 15.4     | 95.0     | 91.0  | 0.0      | 50.0          | 21.9      | 1        |
| 2  | 3   | 1024.1   | 19.4    | 16.1        | 14.6    | 9.3      | 75.0     | 47.0  | 8.3      | 70.0          | 18.1      | 1        |
| 3  | 4   | 1013.4   | 18.1    | 17.8        | 16.9    | 16.8     | 95.0     | 95.0  | 0.0      | 60.0          | 35.6      | 1        |
| 4  | 5   | 1021.8   | 21.3    | 18.4        | 15.2    | 9.6      | 52.0     | 45.0  | 3.6      | 40.0          | 24.8      | 0        |

### Deskripsi Dataset 
```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2190 entries, 0 to 2189
Data columns (total 13 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   id             2190 non-null   int64  
 1   day            2190 non-null   int64  
 2   pressure       2190 non-null   float64
 3   maxtemp        2190 non-null   float64
 4   temparature    2190 non-null   float64
 5   mintemp        2190 non-null   float64
 6   dewpoint       2190 non-null   float64
 7   humidity       2190 non-null   float64
 8   cloud          2190 non-null   float64
 9   sunshine       2190 non-null   float64
 10  winddirection  2190 non-null   float64
 11  windspeed      2190 non-null   float64
 12  rainfall       2190 non-null   int64  
dtypes: float64(10), int64(3)
memory usage: 222.5 KB
```

### ❓ Check Missing Values 🛑
  - **Train Data** :
```python
id               0
day              0
pressure         0
maxtemp          0
temparature      0
mintemp          0
dewpoint         0
humidity         0
cloud            0
sunshine         0
winddirection    0
windspeed        0
rainfall         0
dtype: int64
```

  - **Test Data** :
```
id               0
day              0
pressure         0
maxtemp          0
temparature      0
mintemp          0
dewpoint         0
humidity         0
cloud            0
sunshine         0
winddirection    1
windspeed        0
dtype: int64
```
Terdapat 1 nilai yg hilang untuk fitur *winddirection* dari dataset test.csv 

### 📊 Check Data Distribution 🌐
![Data Distribution Comparison](data/DataDistribution.png)

dari distribusi data tsb, saya membandingkan distribusi antara train and test data. lalu dapat disimpulkan bahwa distribusi data antara data train and test itu terlihat sama satu sama lain. ok sekarang mari kita tampilkan perbandingan distribusi antara prediksi hujan dan tidak hujan dalam Train data.

![Data Distribution Rainfall Distribution](data/Rain-Prediction-Train-data.png)

Note :
   - Batang berwarna **Kuning** merupakan distribusi untuk Prediksi Hujan
   - Batang berwarna **Biru muda** merupakan distribusi untuk prediksi tidak hujan
   - Batang berwarna **abu-abu** merupakan distribusi gabungan antara distribusi hujan dan tidak hujan

🧮 Penjelasan :
   - 1️⃣ Distribusi hujan dan tidak hujan terlihat hampir merata dan serupa di sepanjang hari. Tidak ada pola signifikan yang memperlihatkan peningkatan probabilitas hujan pada hari-hari tertentu. Fitur **days** tampaknya kurang berpengaruh dalam memprediksi hujan atau tidak hujan, karena distribusinya relatif mirip untuk kedua kategori.<br>
   - 2️⃣ Saat suhu (**temparature, mintempt, maxtemp**) makin tinggi, proporsi data yang hujan cenderung meningkat. Ini terlihat dari “puncak” histogram untuk hujan yang lebih banyak pada rentang suhu menengah-tinggi.
   - 3️⃣ Terlihat perbedaan mencolok; pada kelembapan (**humidity**) tinggi (80% ke atas), porsi hujan mendominasi. Pada kelembapan rendah, lebih didominasi tidak hujan.
   - 4️⃣ Distribusi arah angin (**winddirection**) tampak lebih tersebar dan tidak sejelas fitur lain. Mungkin ada sedikit pola di arah angin tertentu yang lebih sering hujan, namun tidak sedrastis kelembapan atau suhu. Arah angin bisa memiliki pengaruh, tapi tidak sekuat kelembapan atau suhu. 
   - 5️⃣ Saat tekanan (**pressure**) udara rendah, proporsi hujan terlihat lebih tinggi; sebaliknya, pada tekanan udara tinggi, lebih banyak data tidak hujan.
   - 6️⃣ Pada tingkat awan (**cloud**) tinggi (mendekati 100%), mayoritas data menunjukkan hujan. Ketika awan rendah (langit lebih cerah), lebih banyak data tidak hujan. Fitur cloud sangat signifikan membedakan hujan dan tidak hujan. semakin banyak awan, semakin besar peluang hujan.
   - 7️⃣ Ada kecenderungan bahwa hujan muncul pada rentang kecepatan angin (**windspeed**) yang agak lebih tinggi, tapi tidak sedramatis fitur kelembapan/awan. Kecepatan angin memiliki pengaruh sedang. Angin yang lebih kencang kadang menandakan sistem tekanan rendah yang membawa hujan, namun korelasinya tidak selalu kuat.
   - 8️⃣ Pada titik embun tinggi, hujan cenderung lebih banyak; ini karena titik embun tinggi menandakan kelembapan yang tinggi di udara.
   - 9️⃣ Ketika durasi sinar matahari (**sunshine**) panjang, mayoritas data adalah tidak hujan. Sebaliknya, pada durasi sinar matahari yang singkat, proporsi hujan meningkat.

<br>

selanjutnya kita akan cek perbandingan distribusi antara Prediksi Hujan dan Tidak Hujan <br>

![rainfall-distribution](data/rainfall-distribution.png)


pada distribusi ini , terjadi ketidakseimbangan data (Imbalance Data) antara prediksi hujan dan tidak hujan. 
```python
Class Percentages : rainfall
1    75.34
0    24.66
Name: proportion, dtype: float64
```
untuk menangani ini, saya akan mencoba melakukan teknik *Oversampling* untuk menangani Imbalance Data ini.

------------------------------------------------------------------------------------------------------

dari distribusi data tsb, mari kita cek seberapa normal distribusi data tsb menggunakan *QQ-Plot*

![QQ-plot](data/QQ-plot.png)

Titik-titik data yang lurus sepanjang garis merupakan distribusi normal. Sementara titik-titik data yang membelok ke kiri/kanan merupakan distribusi yang miring. Nilai R2 menunjukkan seberapa dekat kumpulan data tersebut mendekati distribusi normal. Semakin tinggi nilai R2, semakin dekat dengan distribusi normal.
dari QQ-plot tsb. **pressure, humidity, windspeed** merupakan 3 fitur yg paling mendekati distribusi normal. <br>
*Tujuan memvisualisasi QQ-plot ialah untuk melihat bentuk dari distribusi data tsb, karena dataset yg mempunyai distribusi normal sangat baik untuk menggunakan model klasifikasi Linear , seperti : **Logistic Regression, Linear Discriminant Analysis (LDA), Support Vector Machine Linear, Perceptron Neural Network, Online Classifier, Passive Aggressive Classifier, Maximum Entropy Classifier**.*

### 🔗 Check Correlation 🔍

![independent-pearson-correlation](data/independent-correlation_pearson.png)

1. **Korelasi sangat tinggi (Multikolinearitas sangat tinggi)**
   1. **maxtemp ↔ temperature (0.94)** <br>
      Nilai korelasinya sangat tinggi (mendekati 1). Artinya, saat **maxtemp** naik, **temperature** juga naik (dan sebaliknya). Keduanya bisa dianggap mengukur aspek suhu yang hampir sama dalam data ini.
   2. **temperature ↔ mintemp (0.88)** <br>
      Sama-sama berhubungan kuat. Menunjukkan bahwa ketika **temperature** umum meningkat, **mintemp** juga cenderung meningkat.
   3. **humidity ↔ dewpoint (0.89)** <br>
      Keduanya memiliki hubungan yang sangat erat. Bila **dewpoint** meningkat, **humidity** juga meningkat. Ini menunjukkan keduanya memuat informasi kelembapan yang serupa.

2. **Korelasi Tinggi (Multikolinearitas tinggi)**
   1. **cloud ↔ sunshine (-0.70)** <br>
      Korelasi negatif kuat. Semakin besar nilai **cloud**, semakin rendah **sunshine**, dan sebaliknya. Artinya, kedua variabel ini saling “menggantikan” satu sama lain di dalam data.
   2. **pressure ↔ sunshine (0.59) dan pressure ↔ cloud (-0.51)** <br>
      **pressure** memiliki korelasi positif cukup kuat dengan **sunshine (0.59)** dan negatif dengan **cloud (-0.51)**. Artinya, dalam data ini, saat **pressure** meningkat, **sunshine** cenderung naik, sedangkan **cloud** cenderung turun.
   3. **maxtemp ↔ sunshine (0.66), temperature ↔ sunshine (0.70), dan mintemp ↔ sunshine (0.53)** <br>
      Secara umum, kelompok **temperature** (baik **maxtemp**, **temperature**, maupun **mintemp**) menunjukkan korelasi positif moderat dengan **sunshine**, dan negatif dengan **cloud**. Hal ini menggambarkan bahwa saat suhu meningkat, **sunshine** cenderung meningkat, sedangkan **cloud** cenderung menurun.

3. **Korelasi Rendah (Tak ada Multikolinearitas)**
   1. **winddirection** <br>
      Secara umum memiliki korelasi yang sangat rendah dengan variabel lain (misal: ~0.01 dengan **windspeed**, ~-0.01 s/d ~0.13 dengan variabel lain). Ini menunjukkan **winddirection** dalam dataset ini relatif berdiri sendiri, tidak bergerak seiring variabel lain.
   2. **windspeed**  <br>
      Hampir tidak berkorelasi kuat dengan variabel lain (mayoritas di bawah 0.10). Jadi **windspeed** juga tidak terlalu “terikat” dengan variabel lain dalam dataset ini.
   3. **day**   <br>
      Korelasinya juga lemah dengan variabel lain (kebanyakan di bawah ±0.15). Ini menunjukkan **day** (mungkin penomoran hari) tidak berasosiasi kuat dengan perubahan variabel cuaca lainnya pada dataset ini.


🧮 untuk fitur Independent yg multikolinearitas, kita bisa lakukan hal-hal ini :
   - 1️⃣ Hapus Variable2 yg saling berkorelasi
   - 2️⃣ Gunakan _Principal Component Analysis (PCA)_ untuk mengatasi multikolinearitas
   - 3️⃣ Menggabungkan variabel2 yang multikolinearitas kemudian menghapus variabel asli
   - 4️⃣ Transformasi data dari variable yg multikolinearitas (seperti transformasi log, transformasi akar kuadrat atau lainnya)
   - 5️⃣ Menambahkan regularisasi Ridge (L2) atau regularisasi Lasso (L1) untuk menambahkan penalti dan mengurangi multikolinearitas
   - 6️⃣ Pertimbangkan teknik pemilihan fitur seperti Recursive Feature Elimination (RFE)
   - 7️⃣ Bereksperimen dengan Feature Engineering untuk menggabungkan fitur-fitur yang berkorelasi
   - 8️⃣ Gunakan model ensemble yang dapat menangani fitur berkorelasi secara lebih efektif
   - 9️⃣ Cobalah model berbasis pohon yang kurang sensitif terhadap multikolinearitas
   - 🔟 Uji ambang korelasi yang berbeda untuk memutuskan fitur mana yang akan dihapus

*Tujuan membuat heatmap dari **Korelasi Pearson** ini adalah untuk melihat interaksi antar variable dan juga untuk menghindari dan menangani variable2 independen yg saling berkorelasi kuat.* <br> 
ok selanjutnya saya akan menampilkan bagaimana hubungan/korelasi antara variable independent dgn variable dependent (**rainfall**) dgn menggunakan **Korelasi Spearman**. 

![dependent_correlation-spearman](data/dependent-correlation_pearson.png)

📝 Penjelasan :
   1. **cloud (0.56)** : Memiliki korelasi positif tertinggi dengan rainfall. Artinya, berdasarkan data ini, semakin tinggi nilai cloud, cenderung diikuti oleh meningkatnya rainfall (berlaku sebaliknya).
   2. **sunshine (-0.51)** : Memiliki korelasi negatif paling kuat dengan rainfall. Semakin tinggi nilai sunshine, data ini menunjukkan kecenderungan rainfall menurun.
   3. **humidity (0.25)** : **humidity** merupakan fitur ke 3 yg mempunyai **korelasi spearman** terbesar dgn fitur target (**rainfall**) <br>
   4. Fitur-fitur lainnya seperti <strong>windspeed, winddirection, dewpoint, mintemp, maxtemp, pressure, day </strong> memiliki korelasi yang tidak terlalu besar dengan fitur target (<strong>rainfall</strong>). Kita dapat mempertimbangkan untuk menghapusnya atau memeriksa fitur kepentingan untuk memilih hanya fitur-fitur yang paling penting</span><br>

----------------------------------------------------------------------------------------------------

![kde plot](data/kde-plot.png)

menampilkan kde plot untuk membandingkan distribusi probabilitas antara prediksi hujan dan tidak hujan. *sebenarnya visualisasi kde-plot ini sama dgn visualisasi bar chart dari distribusi rainfall tadi, namun kde-plot ini lebih mudah untuk dibaca*. <br>
      
### 🔗 Feature Importance with Tree-Based Model 🌳

![feature importances using Tree model](data/rf-feature-importances.png)

ini adalah bar chart untuk menampilkan fitur paling penting menggunakan Tree-Based Model Random Forest. 5 fitur terpenting nya adalah **cloud, sunshine, humidity, dewpoint, day**.
*Tujuannya untuk menganalisis base fitur paling penting yg berpengaruh untuk memprediksi klasifikasi dan melakukan feature engineering berdasarkan fitur2 yg paling relevan*

### 🚨 Check for Outliers 🔎
<br>

![boxplot for checking outlier](data/boxplot.png)

dari box-plot tsb, terdapat beberapa outlier:
   1. **pressure** : terdapat hanya ada 2 sedikit outlier. outlier seperti ini bisa kita abaikan atau bisa digunakan winsorization untuk membatasi nilai ke dalam threshold tertentu.
   2. **mintemp** : fitur ini hanya terdapat 1 outlier. kita bisa mengabaikan outlier ini.
   3. **dewpoint, humidity, cloud, windspeed** : fitur ini terdapat cukup banyak outlier. kita bisa mempertimbangkannya untuk menggunakan teknik *Capping* atau *Winsorization*. kalau misalkan outlier tidak perlu penting, bisa kita hapus outliernya (tidak disarankan untuk ini karena akan menghilangkan informasi penting dari data). kita bisa juga mempertahankan outlier ini , tapi harus menggunakan **Robust Scaling** untuk feature scaling nya , agar model lebih tahan / robust terhadap outlier.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.
Teknik-teknik yg digunakan dalam Data Preparation antara lain :
1. Menangani Nilai yg hilang 🧹
2. Feature-Engineering : Membuat Fitur Baru 🛠️
3. Menangani Outlier 🚨
4. Split Dataset ✂️
5. Feature Scaling 📏
6. Menangani Imbalance Dataset : OVERSAMPLING ⚖️

---------------------------------------------------------------------------------------------------------------------------------------

### Menangani Nilai yg hilang 🧹
Dalam menangani nilai hilang untuk fitur *winddirection* , saya mengganti nya dengan nilai median.
```python
# HANDLING MISSING VALUES

# REPLACE NULL VALUES WITH MEDIAN
test_data['winddirection'] = test_data['winddirection'].fillna(value= test_data['winddirection'].median())  

test_data['winddirection'].isna().sum()
```
Alasannya karena jumlah nilai yg hilangnya cuman 1 , jadi tetap mempertahankan distribusi data.
### Feature-Engineering : Membuat Fitur Baru 🛠️
Dalam Feature Engineering, Saya membuat 10 Fitur Baru untuk menangkap pola tersembunyi dalam data. Fitur baru itu antara lain :
1. **temp_range** : untuk mengetahui rentang suhu pd hari itu berapa. Rentang yang besar mungkin mengindikasikan cuaca cerah (tekanan tinggi), sedangkan rentang kecil bisa menandakan langit berawan atau hujan.
```python
combined_data['temp_range'] = combined_data['maxtemp'] - combined_data['mintemp']
```
2. **temp_dew_spread** : Selisih antara suhu aktual (temperature) dan titik embun (dewpoint) mencerminkan kelembapan relatif udara.
```python
combined_data['temp_dew_spread'] = combined_data['temparature'] - combined_data['dewpoint']
```
3. **heat_index** : untuk menggabungkan suhu, titik embun, dan kelembapan untuk mengukur suhu yang "dirasakan". Nilai tinggi menunjukkan kondisi lembap dan panas.
```python
combined_data['heat_index'] = 0.5 * (combined_data['temparature'] + combined_data['dewpoint']) + 0.1 * combined_data['humidity'] - 10
```
4. **wind_east** dan **wind_north** : memahami pola angin .**wind_east** angin bertiup dari timur ke barat, **wind_north** angin bertiup dari utara ke selatan
```python
combined_data['wind_east'] = combined_data['windspeed'] * np.cos(combined_data['winddirection'])
combined_data['wind_north']= combined_data['windspeed'] * np.sin(combined_data['winddirection'])
```
5. **humidity_cloud** : memahami dan menangkap interaksi antara **humidity** (kelembapan) dgn **cloud** (persentase awan).
```python
combined_data['humidity_cloud'] = combined_data['humidity'] * combined_data['cloud']
```
6. **sunshine_cloud_ratio** : mengukur seberapa banyak sinar matahari yang tertutup awan.
```python
combined_data['sunshine_cloud_ratio'] = combined_data['sunshine'] / (combined_data['cloud'] + 1e-5)
```
7. **moisture_index** : kombinasi antara **dewpoint** (titik embun) dgn **humidity** (kelembapan) yg mencerminkan kandungan uap air di udara.
```python
combined_data['moisture_index'] = combined_data['dewpoint'] * combined_data['humidity']
```
8. **wind_chill** : menggambarkan suhu yang dirasakan akibat kombinasi suhu dan angin.
```python
combined_data['wind_chill'] = 13.12 + 0.6215 * combined_data['temparature'] - 11.37 * (combined_data['windspeed']**0.16) + 0.3965 * combined_data['temparature'] * (combined_data['windspeed']**0.16)
``` 
9. **high_rain_risk** : mengenali pola cuaca ekstrem jika **humidity > 80** dan **cloud > 80** (binary label)
```python
def set_high_rain(row):
   if row['humidity'] > 80 and row['cloud'] > 80:
      return 1
   else:
      return 0

combined_data['high_rain_risk'] = combined_data.apply(set_high_rain, axis=1)
```

### Menangani Outlier 🚨

untuk menangani outlier ini , saya menggunakan Teknik Winsorization untuk membatasi sebuah nilai yg melewati threshold. <br>

*Winsorization adalah teknik yang digunakan untuk menangani outlier dgn cara membatasi nilai-nilai ekstrem tersebut pada ambang batas tertentu, sehingga nilai-nilai tersebut tidak lagi menjadi terlalu ekstrem. singkatnya nilai yg melebihi threshold akan diubah ke dalam batas threshold tsb.*

```python
new_train_data['sunshine_cloud_ratio'] = winsorize(a = new_train_data['sunshine_cloud_ratio'], limits=[0, 0.01])
new_test_data['sunshine_cloud_ratio'] = winsorize(a = new_test_data['sunshine_cloud_ratio'], limits=[0, 0.01])
```
disini saya melakukan *Winsorization* dari train and test data untuk kolom **sunshine_cloud_ratio**. saya menetapkan threshold = 0.01 (99% persentil) . artinya nilai titik data yg melebih 99% persentil akan dibatasi ke nilai threshold tsb.


### Split Dataset ✂️
```python
x_train, x_val, y_train, y_val = train_test_split(x,y, test_size=0.20, random_state= 2025, shuffle=True)
```
Membagi data menjadi Train and Validation Data dgn proporsi 80/20. train data digunakan untuk melatih data, sedangkan validation data digunakan untuk mengevaluasi hasil model. 


### Feature Scaling 📏
```python
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
```
melakukan feature scaling dgn menggunakan 2 Teknik Normalisasi data. yaitu **Teknik Robust Scaling** , dan **Z-Score Normalization**.
**Robust Scaling** digunakan ketika data mempunyai outlier yg signifikan dan distribusi data skewed. dan **Z-Score Normalization** digunakan ketika data mendekati distribusi normal.

### Menangani Imbalance Dataset : OVERSAMPLING ⚖️
```python
# SVM SMOTE
svm_smote = SVMSMOTE(sampling_strategy=0.45, random_state= seed_value, m_neighbors = 3, k_neighbors=4)
x_resampled, y_resampled = svm_smote.fit_resample(x_train, y_train)
```
untuk menangani imbalance data, saya menggunakan teknik SVM SMOTE untuk membuat sintetis dataset. <br>
**SVM SMOTE** yaitu Teknik Oversampling yg menggabungkan algoritma **SVM** dan **SMOTE** untuk membuat *synthetic data* (data baru). **SVM SMOTE** membuat *Synthetic Data* di daerah yg dekat dgn garis _Hyperplane_ .  <br> <br>

inilah perbandingannya : 

![](data/oversampling-scatter-plot.png)


## Modeling
dalam melakukan tahap Modelling , saya akan mencoba 2 teknik yg berbeda. pertama yaitu menggunakan model Machine Learning, dan yg kedua menggunakan model Deep Learning. <br> <br>
untuk model Machine Learning, saya akan menggunakan Teknik Ensemble dan Boosting yg dikombinasikan dgn **Optuna** untuk menghasilkan model dgn *Hyperparameter Terbaik*. Tujuan saya dalam menggunakan teknik ini adalah agar model dapat mempelajari Pola Non-Linear dan dapat menangani Data yang Tidak Seimbang. <br><br>
```python
Model Boosting bekerja dengan menggabungkan beberapa model yang lebih lemah (weak learner) menjadi satu model yang lebih kuat
dan berfokus pada perbaikan kesalahan yang dibuat oleh model sebelumnya pada iterasi sebelumnya, sehingga model akhir memiliki
kemampuan prediksi yang lebih akurat dan kuat untuk data yang kompleks atau tidak seimbang. 
```
Teknik Boosting yang saya gunakan, yaitu:
<ol>
   <li><strong>Gradient Boosting Machine</strong></li>
   <li><strong>Light Gradient Boosting Machine</strong></li>
   <li><strong>Adaptive Boosting</strong></li>
   <li><strong>Xtreme Gradient Boosting Machine</strong></li>
   <li><strong>Category Boosting</strong></li>
</ol>
<br>
Kemudian setelah saya membuat semua jenis model *Boosting*, saya akan menggabungkan / menyatukan semua model tersebut menggunakan <strong>Stacking Model </strong>.<br> <br> 
<strong>Tujuannya adalah menggabungkan semuanya dan untuk menciptakan model yang lebih kuat dan canggih serta mengatasi kelemahan setiap model yang ada.</strong>
<br> 

-------------------------------------------------------------------------------------------------------------------------

lalu untuk teknik kedua yg saya gunakan yaitu teknik **Deep Learning**. Saya menggunakan **FeedForward Neural Network** untuk membangun sebuah model deep learning, lalu menggunakan **Keras-Tuner** mendapatkan hyperparameters terbaiknya. <br> <br>


### A. Machine Learning Model

1. **Gradient Boosting Machine**










**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.



## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

