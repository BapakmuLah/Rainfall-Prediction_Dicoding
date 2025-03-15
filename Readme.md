# Laporan Proyek Machine Learning - Aliffa Agnur

## Domain Proyek

Hujan merupakan salah satu fenomena alam yang menunjukan jatuhnya titik air dari atmosfer ke permukaan bumi. Curah hujan adalah jumlah air yang jatuh di tanah datar selama periode tertentu yang diukur dengan satuan tinggi (mm) di atas permukaan horizontal. Jumlah curah hujan diukur sebagai volume air yang jatuh di atas permukaan bidang datar dalam periode waktu tertentu, yaitu harian, mingguan, bulanan, atau tahunan. Intensitas curah hujan yang tinggi yang sering disebut hujan ekstrem dapat mengakibatkan terjadinya bencana alam (Laia & Setyawan, 2020). [PREDIKSI CURAH HUJAN MENGGUNAKAN RECURRENT NEURAL NETWORK (RNN) DAN LONGSHORT-TERM MEMORY (LSTM)](https://eprints.unpak.ac.id/7983/1/Skripsi_065119023_Feri%20Irawan.pdf)
Curah hujan yang tidak menentu dapat menyebabkan banjir, kekeringan, dan kerugian ekonomi. Oleh karena itu, prediksi curah hujan yang akurat sangat penting untuk perencanaan dan pengambilan keputusan yang efektif. [Prakiraan Hujan menggunakan Metode Random Forest dan Cross Validation](https://ejurnal.itenas.ac.id/index.php/mindjournal/article/view/9220)
Curah hujan dapat diprediksi dengan menerapkanMachine Learning yang merupakan cabang ilmu turunan dari Artificial Intelligenceatau kecerdasan buatan. Machine Learning membahas bagaimana algoritma komputer dapat mempelajari data yang diinputkan dengan mengenali sifat karakter data atau pola data, kemudian akan mengubah pola data yang berhasil dipelajari menjadi sebuah tindakan yang meminimalisir pekerjaan yang membutuhkan manusia. [Penerapan Machine Learning Dalam Prediksi Curah Hujan Dengan Algoritma Random Forest Di Wilayah Kota Pagaralam Sumatera Selatan](https://repository.unsri.ac.id/83938/3/RAMA_45201_08021381823054_0015096101_0009067603_01_front_ref.pdf)

**Mengapa Masalah ini harus diselesaikan?**:

​Prediksi curah hujan yang akurat sangat penting dalam sektor pertanian, karena membantu petani merencanakan waktu tanam dan panen dengan lebih efisien, sehingga dapat meningkatkan hasil pertanian dan mengurangi risiko gagal panen. [Pentingnya Memahami Cuaca dan Pengaruhnya ke Pertanian](https://ugm.ac.id/id/berita/pentingnya-memahami-cuaca-dan-pengaruhnya-ke-pertanian/)
Dalam perencanaan kota, data curah hujan yang akurat memungkinkan pemerintah dan perencana kota mengelola infrastruktur perkotaan, seperti sistem drainase, untuk mencegah banjir dan kerusakan lainnya. [Pentingnya Sensor Curah Hujan pada Weather Station](https://loggerindo.com/2024/11/14/pentingnya-sensor-curah-hujan-pada-weather-station/)
Curah hujan memiliki peran terpenting dalam menentukan ketersediaan air di berbagai wilayah. Ketika air hujan turun, maka sebagian air akan mengalir di permukaan tanah sebagai limpasan, mengisi waduk, danau, sungai, sedangkan sebagian lainnya meresap ke dalam tanah untuk memperbarui akuifer. Tersedianya curah hujan yang cukup sangat penting untuk menjamin ketersediaan air bagi berbagai kebutuhan manusia, dimulai dari kebutuhan rumah tangga, operasional industri, hingga irigasi pertanian. [Pemantauan Curah Hujan untuk Manajemen Sumber Daya Air yang Berkelanjutan](https://www.mertani.co.id/post/pemantauan-curah-hujan-untuk-manajemen-sumber-daya-air-yang-berkelanjutan)

- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.
  
  Format Referensi: [Judul Referensi](https://scholar.google.com/) 

**Bagaimana Masalah ini diselesaikan?** :

Penelitian ini memanfaatkan jaringan saraf tiruan untuk memprediksi curah hujan harian di Stasiun Meteorologi Kemayoran. Data cuaca harian dari Januari 2011 hingga Desember 2019 digunakan untuk pelatihan model, yang kemudian diuji dengan data dari Januari hingga Agustus 2020. Variasi model dibuat berdasarkan jenis input dan jumlah lapisan tersembunyi. Hasil penelitian menunjukkan bahwa penggunaan parameter input kondisi cuaca permukaan seperti suhu udara, kelembaban udara, dan durasi penyinaran matahari memberikan nilai koefisien korelasi sebesar 0,4–0,5 dan MAE 9,7–9,8 mm. Sebaliknya, penggunaan data hujan hari-hari sebelumnya sebagai input menghasilkan korelasi 0,1–0,3 dan MAE 11,3–12,3 mm, menunjukkan bahwa parameter cuaca permukaan lebih efektif sebagai prediktor. [Prediksi Curah Hujan Harian di Stasiun Meteorologi Kemayoran Menggunakan Artificial Neural Network (ANN)](https://scholar.google.com/citations?view_op=view_citation&hl=id&user=8mExcgIAAAAJ&citation_for_view=8mExcgIAAAAJ:KlAtU1dfN6UC)
Penelitian ini menggunakan model NeuralProphet untuk memprediksi curah hujan bulanan dan harian di DKI Jakarta. Data yang digunakan adalah data satelit PERSIAN-CCS dari Januari 2005 hingga Juni 2021. Hasil penelitian menunjukkan bahwa secara spasial, model NeuralProphet dapat mengklasifikasikan persebaran curah hujan di wilayah DKI Jakarta. Namun, terdapat perbedaan nilai yang cukup tinggi antara prediksi dan data observasi. Prediksi bulanan menghasilkan akurasi terbaik dengan korelasi 0,8, RMSE 58,45 mm, dan MAE 23,37 mm, sedangkan prediksi harian memiliki korelasi 0,55, RMSE 10,73 mm, dan MAE 9,32 mm. [Prediksi Curah Hujan di Wilayah DKI Jakarta dengan Model NeuralProphet](https://scholar.google.com/citations?view_op=view_citation&hl=id&user=8Z4345gAAAAJ&citation_for_view=8Z4345gAAAAJ:2P1L_qKh6hAC)
Berdasarkan hasil yang telah diperoleh selama   proses   pengerjaan   yaitu   melakukan prediksi  terhadap  curah  hujan  dan  kecepatan angin     maka     dapat     disimpulkan     bahwa pemodelan  terbaik  dalam  melakukan  prediksi curah hujan adalah dengan algoritma Backprpagation  Neural  Network yaitu  dengan dengan  nilai  RMSE  0.079535  yaitu  dengan  20 neuron,  1000 epoch, serta validation  split 0.1. Untuk   pemodelan   terbaik   dalam   melakukan prediksi    kecepatan    angin    adalah    dengan menggunakan    algoritma Reccurent    Neural Network dengan  menggunakan  arsitektur Long Short Term Memory (LSTM) yaitu dengan nilai RMSE   yang   diperoleh   berada   pada   nilai 0.06281251 dengan 30 neuron, 800 epoch, serta validation split 0.1. [PREDIKSI TINGGI CURAH HUJAN DAN KECEPATAN ANGIN BERDASARKAN DATA CUACA DENGAN PENERAPAN ALGORITMA ARTIFICIAL NEURAL NETWORK(ANN)](https://journal.universitasmulia.ac.id/index.php/seminastika/article/view/237)


## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
    - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

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

