# Tutorial: Materi Pembelajaran Machine Learning

## Daftar Isi
  [*introdcution*](#introduction)
1. Model Machine Learning
    - [Regresi Linear *(Linear Regression)*](#regresi-linear-linear-regression)
    - [Regresi Logistik *(Logistic Regression)*](#regresi-logistik-logistic-regression)
    - [Klasifikasi *(Classification)*](#klasifikasi-classification)
2. Data
    - [Data Numerik *(Numerical Data)*](#regresi-linear)
    - [Data Terkategori *(Categorical Data)*](#loss)
    - [Dataset, Generalisasi, dan *Overfitting*](#dataset-generalisasi-overfitting)
3. Model Machine Learning Tingkat Lanjut
    - [Jaringan Saraf *(Neural Networks)*](#artificial-neural-network)
    - [Embeddings](#embeddings)
    - [Large Language Models (LLMs)](#large-language-models)
4. Penerapan Machine Learning di Dunia Nyata
    - [Pembuatan Sistem Machine Learning](#pembuatan-sistem-machine-learning)
    - [Automasi dengan Machine Learning](#loss)
    - [Keadilan dalam Sistem AI *(Fairness)*](#keadilan-dalam-sistem-ai)

## *Introduction*
### Apa itu Machine Learning?
Machine Learning (ML) adalah proses dari pengembangan suatu *model* yang digunakan untuk melakukan prediksi atau menghasilkan konten (teks, gambar, video maupun audio) berdasarkan data yang diberikan. *Model* itu sendiri merupakan suatu sistem ML yang memanfaatkan relasi matematis dari suatu data untuk membuat prediksi data baru ataupun membuat konten.

Beberapa kategori ML berdasarkan bagaimana suatu sistem membuat prediksi ataupun konten, yaitu:
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
4. Generative AI

### Supervised Learning
Supervised Learning adalah *model* ML yang dilatih menggunakan data yang diberikan beserta label atau jawaban yang benar. Hal ini bertujuan agar *model* dapat berkembang terus-menerus, sehingga *model* tersebut dapat menjadi lebih akurat. Penggunaan umum Supervised Learning yaitu pada regresi dan klasifikasi.
*Model* regresi bertujuan untuk memprediksi suatu nilai, seperti harga, waktu, suhu, dll. Sedangkan *model* klasifikasi bertujuan untuk menentukan kategori atau kelas dari suatu data, seperti klasifikasi rendah atau tingginya harga ataupun klasifikasi email sebagai spam atau bukan spam.

### Unsupervised Learning
Unsupervised Learning adalah *model* yang dilatih menggunakan data tanpa label atau jawaban yang benar. Tujuannya agar *model* dapat mengidentifikasi suatu pola atau keterkaitan dari data. Umumnya menggunakan metode *clustering*, dimana suatu data dengan pola yang sama akan dikelompokkan ke dalam satu kategori atau *cluster*. Salah satu penerapannya adalah analisis data *user* di suatu website, dimana sistem dapat mengelompokkan *user* berdasarkan perilaku mereka tanpa perlu mengetahui tipe *user* sebelumnya.

### Reinforcement Learning
Reinforcement Learning adalah *model* yang dilatih dengan sistem *Rewards or Punishments* berdasarkan aksi yang dilakukan. Sistem ini akan membuat kebijakan yang dapat menetapkan strategi efisien untuk mendapatkan *reward* terbanyak.

### Generative AI
Generative AI adalah *model* yang membuat konten dari *user input*. Contohnya pembuatan gambar, komposisi musik, merangkum teks, penjelasan, kode, dll. *Model* ini mengambil variasi *input* dan menghasilkan variasi *output*. *Input* juga dapat dikombinasikan seperti mengambil *input* gambar untuk menghasilkan *output* gambar dan teks. *Generative model* belajar dari pola-pola dalam data dengan tujuan untuk menghasilkan data baru yang mirip.

Untuk membuat *output* yang unik dan kreatif, *generative model* dilatih terlebih dahulu menggunakan unsupervised learning untuk meniru data yang dilatih. Lalu dilatih lebih lanjut menggunakan supervised learning atau reinforcement learning pada data tertentu yang kemungkinan akan berhubungan dengan tugas yang diberikan.

## 1. Model Machine Learning
### Regresi Linear *(Linear Regression)*
Regresi Linear *(Linear Regression)* merupakan salah satu teknik dalam statistika yang digunakan untuk mencari hubungan antar variabel. Dalam Machine Learning, regresi linear digunakan untuk mencari hubungan antara fitur *(features)* dan label.

Sebagai contoh jika kita ingin memprediksi efisiensi berapa liter bahan bakar kendaraan untuk menempuh seberapa jauh kilometer berdasarkan berat mobil. Disini telah disediakan dataset sebagai berikut

|   Berat Mobil (Ton)   |   Jarak Tempuh (Km/L)   |
|:---------------------:|:---------------------:|
|         1.59          |          7.65           |
|         1.67          |          6.38           |
|         1.56          |          7.65           |
|         1.56          |          6.80           |
|         1.97          |          6.38           |
|         2.01          |          5.95           |
|         1.08          |          10.20          |

Jika data tersebut di plot maka hasilnya akan sebagai berikut :
![Plot Data](../Image/Scatter-Plot(RL).png)


## Bahan Bacaan
- [Dokumentasi Machine Learning](https://developers.google.com/machine-learning/crash-course)

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*