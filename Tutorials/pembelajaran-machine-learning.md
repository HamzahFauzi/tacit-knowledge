# Tutorial: Materi Pembelajaran Machine Learning

## Daftar Isi
  [***Introdcution***](#introduction)
1. Model Machine Learning
    1. [Regresi Linear *(Linear Regression)*](#11-regresi-linear-linear-regression)
        - [Loss](#loss)
        - [Gradient Descent](#gradient-descent)
        - [Hyperparameters](#hyperparameters)
    2. [Regresi Logistik *(Logistic Regression)*](#regresi-logistik-logistic-regression)
    3. [Klasifikasi *(Classification)*](#klasifikasi-classification)
2. Data
    1. [Data Numerik *(Numerical Data)*](#regresi-linear)
    2. [Data Terkategori *(Categorical Data)*](#loss)
    3. [Dataset, Generalisasi, dan *Overfitting*](#dataset-generalisasi-overfitting)
3. Model Machine Learning Lanjutan
    1. [Jaringan Saraf *(Neural Networks)*](#artificial-neural-network)
    2. [Embeddings](#embeddings)
    3. [Large Language Models (LLMs)](#large-language-models)
4. Penerapan Machine Learning di Dunia Nyata
    1. [Pembuatan Sistem Machine Learning](#pembuatan-sistem-machine-learning)
    2. [Automasi dengan Machine Learning](#loss)
    3. [Keadilan dalam Sistem AI *(Fairness)*](#keadilan-dalam-sistem-ai)

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

<br>

## **1. Model Machine Learning**
### 1.1 Regresi Linear *(Linear Regression)*
Regresi Linear *(Linear Regression)* merupakan salah satu teknik dalam statistika yang digunakan untuk mencari hubungan antar variabel. Dalam Machine Learning, regresi linear digunakan untuk mencari hubungan antara fitur *(features)* dan label.

Sebagai contoh jika kita ingin memprediksi efisiensi bahan bakar mobil dalam satuan *miles per gallon* yang berdasarkan pada berat kendaraan dalam satuan pounds 

|   Berat Mobil (pounds)   |   Jarak Tempuh (Miles/Gallon)   |
|:---------------------:|:---------------------:|
|         3.5          |          18           |
|         3.69          |         15           |
|         3.44          |         18           |
|         3.43          |         16           |
|         4.34          |         15           |
|         4.42          |         14           |
|         2.37          |         24          |

Jika data tersebut di plot maka hasilnya akan sebagai berikut :
![Scatter Plot (RL)](../Image/Scatter-Plot(RL).png)
Dengan data yang telah di plot kita dapat membuat model prediksi sederhana dengan regresi linear. Kita dapat menggambar lurus yang cocok dengan sebaran titik-titik data yang ada

![Scatter-Plot-Slope](../Image/Scatter-Plot-Full-Line.png)

Regresi Linear memiliki persamaan yang dapat dirumuskan sebagai berikut :

$$
y = mx + b
$$
- y = jarak tempuh ( Nilai keluaran yang ingin diprediksi )
- *m* = kemiringan garis
- x = berat kendaraan ( Nilai input )
- b = titik potong garis terhadap sumbu Y

Dalam ML persamaan untuk regresi linear dapat dituliskan sebagai berikut :

$$
y' = b + w1x1
$$

- y' = nilai label yang diprediksi ( Nilai keluaran )
- b = bias pada model. Bias merupakan titik potong terhadap sumbu y. Digunakan untuk membantu menyesuaikan model agar bisa fit dengan data asli
- w1 = berat pada nilai fitur. Memiliki konsep yang mirip dengan kemiringan garis (*slope*) untuk mengatur kemiringan.
- x1 = nilai fitur (Nilai Input)

Sebagai contoh apabila kita memiliki nilai bias sebesar 33.59 dan nilai *weight* adalah -4.57. Kita dapat membuat prediksi dengan model ini dengan memasukkan ke rumus regresi linear untuk ML :

$$
y' = 33.59 + (-4.57)(x1)
$$

Kita bisa memasukkan berat kendaraan untuk mendapatkan nilai jarak tempuh kendaraan. Sebagai contoh apabila kita memasukkan nilai 4,000 pound maka model ini memprediksi jarak tempuh kendaraan sebesar 15,31 miles/gallon.

![Input Model](../Image/Prediksi-MPG-4000-Pounds.png)

Pada contoh diatas hanya menggunakan satu fitur saja yaitu berat dari mobil. Model dapat menjadi lebih akurat apabila menambahkan lebih dari satu fitur. Formula regresi linear dapat berubah menjadi :


$$
y' = b + w1x1 + w2x2 + ... + wnxn
$$

Dimana :
- x1, x2, ..., xn merupakan fitur-fitur tambahan (bisa berupa berat mobil, ukuran mesin, kecepatan maksimal, dll)
- w1, w2, ..., wn adalah bobot (*weight*) masing-masing fitur yang menentukan seberapa besar pengaruh fitur terhadap prediksi
- b adalah bias untuk menggeser garis prediksi

Dengan menggunakan beberapa fitur, model dapat menangkap lebih banyak informasi dari data sehingga hasil prediksi menjadi lebih relevan dan akurat. Pendekatan ini disebut sebagai regresi linear multivariat.

> ### Loss

**Loss** adalah angka yang mengukur seberapa buruk prediksi model terhadap data sebenarnya. Semakin kecil loss, semakin baik model memprediksi data.



### Cara Menghitung Loss

Rumus:

$$
Loss = (aktual - prediksi)^2
$$

#### Contoh:
Jika nilai aktual = 4, dan prediksi model = 5:

$$
Loss = (4 - 5)^2 = 1
$$



### Perbedaan Loss dan Error

| Istilah | Rumus | Penjelasan |
|--------|-------|------------|
| Error  | Aktual - Prediksi | Nilai selisih antara hasil prediksi dan nilai sebenarnya |
| Loss   | (Aktual - Prediksi)² | Kuadrat dari error agar selalu positif dan lebih sensitif terhadap kesalahan besar |



### Mean Squared Error (MSE)

**MSE** adalah rata-rata dari seluruh nilai **Loss** pada dataset.

$$ 
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$


#### Keterangan:
- $y_i$ : Nilai aktual ke-i  
- $\hat{y}_i$ : Nilai prediksi ke-i  
- $n$ : Jumlah total data

> ### Gradient Descent
Gradient Descent adalah algoritma optimisasi yang digunakan untuk menemukan nilai terbaik dari parameter (bobot/weight dan bias) dalam sebuah model machine learning dengan cara meminimalkan loss function.

Langkah langkah Gradient Descent :
1. Inisialisasi Bobot
2. Hitung Loss dari prediksi Model yang telah dijelaskan diatas
3. Hitung *Gradien*(Kemiringan) dari loss terhadap setiap parameter
4. *Update* parameter dengan bergerak kearah gradien negatif dengan
5. Ulangi proses sampai *konvergen* (loss tidak banyak berubah lagi).
$$
θ=θ−α⋅(∂L/∂θ)
$$
Dimana : 
- $θ$ : Parameter (misalnya weight atau bias)
- $α$ : Learning rate (ukuran langkah)
- $∂L/∂θ$ : Turunan dari loss terhadap parameter

Contoh :
Kita punya sebuah DataShett yaitu : 

|   Berat Mobil (pounds)   |   Jarak Tempuh (Miles/Gallon)   |
|:---------------------:|:---------------------:|
|         3.5          |          18           |
|         3.69          |         15           |
|         3.44          |         18           |
|         3.43          |         16           |
|         4.34          |         15           |
|         4.42          |         14           |
|         2.37          |         24          |

1. Inisialisasi Awal 
Misalnya kita mulai dengan:
- Bobot (weight) awal $w = 0$
- Bias awal $b = 0$
- Learning rate $\alpha = 0.01$

2. Hitung Loss

$$
Loss = \frac{(18-0)^2 + (15-0)^2 + (18-0)^2 + (16-0)^2 + (15-0)^2 + (14-0)^2 + (24-0)^2}{7}
$$
$$
Loss = 303.71
$$

3. Hitung Gradien Loss untuk setiap parameter
$$
Weight Slope : -119.7
$$
$$
Bias Slope : -34.3
$$

4. *Update* parameter

$$
\textit{New weight} = \textit{old weight} - (\textit{small amount} \times \textit{weight slope})
$$

$$
\textit{New bias} = \textit{old bias} - (\textit{small amount} \times \textit{bias slope})
$$

$$
\textit{New weight} = 0 - (0.01 \times (-119.7))
$$

$$
\textit{New bias} = 0 - (0.01 \times (-34.3))
$$

$$
\textit{New weight} = 1.2
$$

$$
\textit{New bias} = 0.34
$$

> ### Hyperparameters
Berbeda dengan parameter yang dihitung oleh *model* saat pelatihan, hyperparameter adalah variabel yang dapat dikendalikan. Tiga hyperparameter yang umum, yaitu:
1. Learning rate
2. Batch size
3. Epochs

### Learning Rate
Learning rate merupakan nilai *float* yang dapat diatur untuk mempengaruhi kecepatan konvergensi suatu *model*. Jika learning rate suatu model terlalu rendah, konvergensi akan memakan waktu yang lama direnakan perubahan parameter terlalu kecil. Tetapi jika learning rate suatu model terlalu tinggi, parameter akan berubah terlalu besar dan menyebabkan fluktuasi yang mengakibatkan konvergensi tidak tercapai.

Learning rate yang ideal dapat membantu *model* untuk konvergensi dengan jumlah iterasi yang rasional. Maka dari itu tujuannya adalah untuk menentukan learning rate yang tidak terlalu tinggi atau terlalu rendah agar *model* dapat mencapai konvergensi dengan cepat. Berikut merupakan kurva loss dari contoh *model* yang berkembang secara signifikan di 20 iterasi awal sebelum berkonvergensi.

![Ideal Learning Rate](../Image/Ideal-Learning-Rate.png)

### Batch Size
Batch size merujuk kepada jumlah data sampel yang diproses *model* sebelum memperbarui variabel *weights* dan *bias*. Dua teknik yang umum yaitu *stochastic gradient descent* and *mini-batch stochastic gradient descent*.

***Stochastic gradient descent* (SGD)**

Teknik ini hanya menggunakan satu contoh (ukuran *batch* adalah satu). Kata *"stochastic"* berarti contoh yang digunakan pada setiap *batch* terpilih secara acak. Teknik ini menghasilkan *noise* yang menyebabkan *loss* bertambah dibandingkan menurun seiring iterasi.

![Kurva SGD](../Image/SGD-curve.png)

Dapat dilihat di kurva tersebut, *model* yang menggunakan *stochastic gradient descent* menghasilkan *noise* di seluruh kurva tidak hanya di dekat konvergensi.

***Mini-batch stochastic gradient descent* (mini-batch SGD)**

Untuk ***N*** jumlah poin data, *batch* akan berukuran lebih dari 1 dan kurang dari ***N***. *Model* memilih contoh-contohnya kedalam setiap batch secara acak, menghitung rata-rata gradien, lalu memperbarui *weights* dan *bias* sekali per iterasi.

![Kurva mini-batch SGD](../Image/mini-batch-sgd.png)

Saat melatih *model*, beberapa *noise* dapat menjadi hal yang bermanfaat, terutama pada *neural network*.

### Epochs
Epoch artinya *model* telah memproses setiap contoh dalam pelatihan sebanyak sekali. Jumlah *epochs* merupakan hyperparameter yang perlu di tentukan sebelum pelatihan *model* dilaksanakan*

## 1.2 Logistik Regression

Logistic Regression adalah algoritma machine learning untuk klasifikasi biner.
Tujuan utamanya adalah memperkirakan probabilitas dari suatu data masuk ke salah satu dari dua kelas (misalnya 0 atau 1, ya atau tidak).

> ### Model Logistik Regression
Model logistic regression mirip linear regression:

$$
z = w_1x_1 + w_2x_2 + .... + w_nx_n + b
$$

Namun, alih-alih langsung menggunakan z sebagai output, logistic regression menggunakan fungsi aktivasi sigmoid untuk mengubah nilai ini menjadi probabilitas antara 0 dan 1:

$$
\hat{y} = σ(z) = \frac{1}{1 + e^{-z}}
$$

### Langkah langkah Logistik Regression
1. Hitung $$ z = wx + b $$

2. Hitung Probabilitas dengan Fungsi Sigmoid $$ \hat{y} = \frac{1}{1 + e^{-z}} $$ 
3. Klasifikasi 
- Jika $$ \hat{y} \geq 0.5 $$ = Kelas 1
- Jika $$ \hat{y} < 0.5 $$ = Kelas 0

### Fungsi Loss : Log loss(Cross-Entropy)
Berbeda dengan linear regression yang memakai MSE, logistic regression menggunakan log loss:

$$
\text{Loss} = - \left[ y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y}) \right]
$$

- jika label $ y = 1 $ maka loss = $ -\text{Log}(\hat{y}) $
- jika label $ y = 0 $ maka loss = $ -\text{Log}(1 -\hat{y}) $
 
### Optimasi dengan Gradient Descent
Parameter \( w \) dan \( b \) diperbarui menggunakan **gradient descent**:

$$
w = w - \alpha \cdot \frac{\partial L}{\partial w}
$$

$$
b = b - \alpha \cdot \frac{\partial L}{\partial b}
$$

Di mana:
- $\alpha$ : learning rate
- $\frac{\partial L}{\partial w}$ :  turunan loss terhadap parameter

### Logistik vs Linear Regression
| Aspek            | Linear Regression       | Logistic Regression       |
|------------------|-------------------------|---------------------------|
| Output           | Nilai kontinu           | Probabilitas (0–1)        |
| Fungsi Aktivasi  | Tidak ada               | Sigmoid                   |
| Fungsi Loss      | Mean Squared Error      | Log Loss (Cross-Entropy)  |
| Tujuan           | Prediksi nilai kontinu  | Klasifikasi biner         |

<br>

## **3. Model Machine Learning Lanjutan**

Jaringan neural adalah model pembelajaran mesin yang dirancang untuk menemukan pola non-linear dalam data. Model ini menghindari eksperimen manual dengan fitur silang dan secara otomatis mempelajari representasi data yang optimal selama pelatihan. Komponen utama dari jaringan neural meliputi node (neuron), lapisan tersembunyi, dan fungsi aktivasi. Selama pelatihan, jaringan neural dioptimalkan menggunakan algoritma backpropagation untuk meminimalkan fungsi kerugian dan meningkatkan akurasi prediksi.

> ### Node dan Lapisan Tersembunyi

Jaringan neural terdiri dari tiga jenis lapisan utama:

- Lapisan Input: Menerima data mentah dari fitur input.
- Lapisan Tersembunyi: Terletak di antara lapisan input dan output, bertanggung jawab untuk memproses informasi dan mengekstraksi fitur kompleks.
- Lapisan Output: Menghasilkan prediksi akhir berdasarkan informasi yang diproses.

Setiap lapisan terdiri dari node (neuron) yang terhubung dengan bobot dan bias. Lapisan tersembunyi memungkinkan jaringan untuk mempelajari representasi data yang lebih kompleks dan non-linear.

> ### Fungsi Aktivasi

Fungsi aktivasi digunakan untuk memperkenalkan non-linearitas ke dalam jaringan, memungkinkan model untuk mempelajari hubungan kompleks dalam data. Beberapa fungsi aktivasi yang umum digunakan meliputi:

- Sigmoid. Menghasilkan output antara 0 dan 1, cocok untuk probabilitas.
- tanh. Menghasilkan output antara -1 dan 1, sering digunakan di lapisan tersembunyi.
- ReLU (Rectified Linear Unit). Menghasilkan output 0 jika input negatif dan output input itu sendiri jika positif. Hal ini populer karena efisiensinya dalam pelatihan.

Jangan lupa ya! Memilih fungsi aktivasi yang sesuai dengan jenis data dan tujuan model.

> ### Pelatihan Backpropagation

Backpropagation adalah algoritma pelatihan utama untuk jaringan neural, memungkinkan pembaruan bobot secara efisien melalui propagasi gradien. Proses ini melibatkan:

- Melakukan inferensi untuk menghasilkan prediksi.
- Menghitung kesalahan (loss) antara prediksi dan nilai sebenarnya.
- Menyebarkan kesalahan kembali melalui jaringan untuk menghitung gradien.
- Memperbarui bobot menggunakan gradien dan laju pembelajaran.

Beberapa tantangan dalam backpropagation meliputi:
- Vanishing Gradients. Gradien yang sangat kecil dapat memperlambat pelatihan, sering terjadi dengan fungsi aktivasi sigmoid atau tanh.
- Exploding Gradients. Gradien yang sangat besar dapat menyebabkan pembaruan bobot yang tidak stabil.
- Dead ReLU. Unit ReLU yang selalu menghasilkan output 0 dapat menghentikan aliran gradien.

Untuk mengatasi masalah ini, teknik seperti penggunaan ReLU, normalisasi batch, dan pengaturan laju pembelajaran yang tepat dapat diterapkan.

> ### Klasifikasi Multi-Class

Klasifikasi multi-class melibatkan pengkategorian data ke dalam lebih dari dua kelas. Dua pendekatan utama dalam menangani masalah ini adalah sebagai berikut:

- One-vs-All (OvA): Membangun satu classifier untuk setiap kelas, yang membedakan antara kelas tersebut dan semua kelas lainnya.
- One-vs-One (OvO) atau Softmax: Membangun classifier untuk setiap pasangan kelas dan menggunakan fungsi aktivasi softmax di lapisan output untuk menghasilkan probabilitas yang dijumlahkan menjadi 1 .

Ini penting ya untuk memilih pendekatan yang sesuai dengan jumlah kelas dan kompleksitas masalah.


## Bahan Bacaan
- [Dokumentasi Machine Learning](https://developers.google.com/machine-learning/crash-course)

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*