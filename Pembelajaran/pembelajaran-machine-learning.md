# Tutorial: Materi Pembelajaran Machine Learning

## Daftar Isi
  [***Introdcution***](#introduction)
1. Model Machine Learning
    - [Regresi Linear *(Linear Regression)*](#regresi-linear-linear-regression)
      - [Loss](#loss)
      - [Gradient Descent](#gradient-descent)
      - [Hyperparameters](#hyperparameters)
    - [Regresi Logistik *(Logistic Regression)*](#logistic-regression)
      - [Model logistic regression](#model-logistic-regression)
      - [Fungsi Loss: Log loss(Cross-Entropy)](#fungsi-loss-log-losscross-entropy)
    - [Klasifikasi *(Classification)*](#klasifikasi-classification)
      - [Thresholds](#thresholds)
      - [Confusion Matrix](#confusion-matrix)
      - [Accrucay, recall, precision, dan metrik lainnya](#accuracy-recall-precision-dan-metrik-lainnya)
      - [ROC dan AUC](#roc-dan-auc)
      - [Multi Class Classification](#multi-class-classification)
2. Data
    - [Data Numerik *(Numerical Data)*](#numerical-data)
      - [Feature Vectors](#feature-vectors)
      - [Visualisasi Data](#visualisasi-data)
      - [Normalisasi](#normalization)
      - [Binning](#binning)
      - [Scrubbing](#scrubbing)
      - [Polynomial Transforms](#polynomial-transforms)
    - [Data Terkategori *(Categorical Data)*](#categorical-data)
      - [Encoding](#encoding-mengonversi-data-kategorik-menjadi-vektor-numerik)
      - [Embedding](#embedding-dan-hashing-untuk-mengurangi-dimensi-tinggi)
      - [Fitur Silang (*Feature Crossing*)](#fitur-silang-feature-crossing)
      - [Pentingnya Kualitas Data](#pentingnya-kualitas-data-pelabelan-manusia-vs-mesin)
    - [Dataset, Generalisasi, dan *Overfitting*](#datasets-generalization-dan-overfitting)
      - [Jenis-jenis Data](#jenis-jenis-data)
      - [Jumlah Data](#jumlah-data)
      - [Kualitas dan Keandalan Data](#kualitas-dan-keandalan-data)
      - [Labels](#labels)
      - [Human Generated Data](#human-generated-data)
      - [Imbalanced Datasets](#imbalanced-datasets)
      - [Generalization](#generalization)
      - [Overfitting](#overfitting)
      - [Model Complexity](#model-complexity)
      - [Regularization](#regularization)
      - [Interpretasi Loss Kurva](#interpretasi-loss-kurva)
3. Model Machine Learning Lanjutan
    - [Jaringan Neural *(Neural Networks)*](#neural-network)
      - [Node dan Lapisan Tersembunyi](#node-dan-lapisan-tersembunyi)
      - [Fungsi Aktivasi](#fungsi-aktivasi)
      - [Pelatihan Backpropagation](#pelatihan-backpropagation)
      - [Klasifikasi Multi-Class](#klasifikasi-multi-class)
    - [Embeddings](#embeddings)
    - [Large Language Models (LLMs)](#large-language-models)
4. Penerapan Machine Learning di Dunia Nyata
    - [Pembuatan Sistem Machine Learning](#pembuatan-sistem-machine-learning)
    - [Automasi dengan Machine Learning](#loss)
    - [Keadilan dalam Sistem AI *(Fairness)*](#keadilan-dalam-sistem-ai)

## *Introduction*
### Apa itu Machine Learning?
Machine Learning (ML) adalah proses dari pengembangan suatu model yang digunakan untuk melakukan prediksi atau menghasilkan konten (teks, gambar, video maupun audio) berdasarkan data yang diberikan. Model itu sendiri merupakan suatu sistem ML yang memanfaatkan relasi matematis dari suatu data untuk membuat prediksi data baru ataupun membuat konten.

Beberapa kategori ML berdasarkan bagaimana suatu sistem membuat prediksi ataupun konten, yaitu:
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
4. Generative AI

### Supervised Learning
Supervised Learning adalah model ML yang dilatih menggunakan data yang diberikan beserta label atau jawaban yang benar. Hal ini bertujuan agar model dapat berkembang terus-menerus, sehingga model tersebut dapat menjadi lebih akurat. Penggunaan umum Supervised Learning yaitu pada regresi dan klasifikasi.
Model regresi bertujuan untuk memprediksi suatu nilai, seperti harga, waktu, suhu, dll. Sedangkan model klasifikasi bertujuan untuk menentukan kategori atau kelas dari suatu data, seperti klasifikasi rendah atau tingginya harga ataupun klasifikasi email sebagai spam atau bukan spam.

### Unsupervised Learning
Unsupervised Learning adalah model yang dilatih menggunakan data tanpa label atau jawaban yang benar. Tujuannya agar model dapat mengidentifikasi suatu pola atau keterkaitan dari data. Umumnya menggunakan metode *clustering*, dimana suatu data dengan pola yang sama akan dikelompokkan ke dalam satu kategori atau *cluster*. Salah satu penerapannya adalah analisis data *user* di suatu website, dimana sistem dapat mengelompokkan *user* berdasarkan perilaku mereka tanpa perlu mengetahui tipe *user* sebelumnya.

### Reinforcement Learning
Reinforcement Learning adalah model yang dilatih dengan sistem *Rewards or Punishments* berdasarkan aksi yang dilakukan. Sistem ini akan membuat kebijakan yang dapat menetapkan strategi efisien untuk mendapatkan *reward* terbanyak.

### Generative AI
Generative AI adalah model yang membuat konten dari *user input*. Contohnya pembuatan gambar, komposisi musik, merangkum teks, penjelasan, kode, dll. Model ini mengambil variasi *input* dan menghasilkan variasi *output*. *Input* juga dapat dikombinasikan seperti mengambil *input* gambar untuk menghasilkan *output* gambar dan teks. *Generative model* belajar dari pola-pola dalam data dengan tujuan untuk menghasilkan data baru yang mirip.

Untuk membuat *output* yang unik dan kreatif, *generative model* dilatih terlebih dahulu menggunakan unsupervised learning untuk meniru data yang dilatih. Lalu dilatih lebih lanjut menggunakan supervised learning atau reinforcement learning pada data tertentu yang kemungkinan akan berhubungan dengan tugas yang diberikan.

<br>

## **1. Model Machine Learning**
## Regresi Linear *(Linear Regression)*
Regresi Linear *(Linear Regression)* merupakan salah satu teknik dalam statistika yang digunakan untuk mencari hubungan antar variabel. Dalam Machine Learning, regresi linear digunakan untuk mencari hubungan antara fitur *(features)* dan label.

Sebagai contoh jika kita ingin memprediksi efisiensi bahan bakar mobil dalam satuan *miles per gallon* yang berdasarkan pada berat kendaraan dalam satuan pounds.

|   Berat Mobil (pounds)   |   Jarak Tempuh (Miles/Gallon)   |
|:------------------------:|:-------------------------------:|
|           3.5            |               18                |
|           3.69           |               15                |
|           3.44           |               18                |
|           3.43           |               16                |
|           4.34           |               15                |
|           4.42           |               14                |
|           2.37           |               24                |

Jika data tersebut di plot maka hasilnya akan sebagai berikut:
![Scatter Plot (RL)](Image/Scatter-Plot(RL).png)
Dengan data yang telah di plot kita dapat membuat model prediksi sederhana dengan regresi linear. Kita dapat menggambar lurus yang cocok dengan sebaran titik-titik data yang ada.

![Scatter-Plot-Slope](Image/Scatter-Plot-Full-Line.png)

Regresi Linear memiliki persamaan yang dapat dirumuskan sebagai berikut:

$$
y = mx + b
$$
- y = jarak tempuh (Nilai keluaran yang ingin diprediksi)
- *m* = kemiringan garis
- x = berat kendaraan (Nilai input)
- b = titik potong garis terhadap sumbu Y

Dalam ML persamaan untuk regresi linear dapat dituliskan sebagai berikut:

$$
y' = b + w1x1
$$

- y' = nilai label yang diprediksi (Nilai keluaran).
- b = bias pada model. Bias merupakan titik potong terhadap sumbu y. Digunakan untuk membantu menyesuaikan model agar bisa fit dengan data asli.
- w1 = berat pada nilai fitur. Memiliki konsep yang mirip dengan kemiringan garis (*slope*) untuk mengatur kemiringan.
- x1 = nilai fitur (Nilai Input).

Sebagai contoh apabila kita memiliki nilai bias sebesar 33.59 dan nilai *weight* adalah -4.57. Kita dapat membuat prediksi dengan model ini dengan memasukkan ke rumus regresi linear untuk ML:

$$
y' = 33.59 + (-4.57)(x1)
$$

Kita bisa memasukkan berat kendaraan untuk mendapatkan nilai jarak tempuh kendaraan. Sebagai contoh apabila kita memasukkan nilai 4,000 pound maka model ini memprediksi jarak tempuh kendaraan sebesar 15,31 miles/gallon.

![Input Model](Image/Prediksi-MPG-4000-Pounds.png)

Pada contoh diatas hanya menggunakan satu fitur saja yaitu berat dari mobil. Model dapat menjadi lebih akurat apabila menambahkan lebih dari satu fitur. Formula regresi linear dapat berubah menjadi:

$$
y' = b + w_1x_1 + w_2x_2 + .... + w_nx_n
$$

Dimana:
- x1, x2, ..., xn merupakan fitur-fitur tambahan (bisa berupa berat mobil, ukuran mesin, kecepatan maksimal, dll).
- w1, w2, ..., wn adalah bobot (*weight*) masing-masing fitur yang menentukan seberapa besar pengaruh fitur terhadap prediksi.
- b adalah bias untuk menggeser garis prediksi.

Dengan menggunakan beberapa fitur, model dapat menangkap lebih banyak informasi dari data sehingga hasil prediksi menjadi lebih relevan dan akurat. Pendekatan ini disebut sebagai regresi linear multivariat.

> ### Loss

**Loss** adalah angka yang mengukur seberapa buruk prediksi model terhadap data sebenarnya. Semakin kecil loss, semakin baik model memprediksi data.

**Cara Menghitung Loss**

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
- $y_i$: Nilai aktual ke-i  
- $\hat{y}_i$: Nilai prediksi ke-i  
- $n$: Jumlah total data

> ### Gradient Descent
Gradient Descent adalah algoritma optimisasi yang digunakan untuk menemukan nilai terbaik dari parameter (bobot/weight dan bias) dalam sebuah model machine learning dengan cara meminimalkan loss function.

Langkah langkah Gradient Descent:
1. Inisialisasi Bobot
2. Hitung Loss dari prediksi Model yang telah dijelaskan diatas
3. Hitung *Gradien*(Kemiringan) dari loss terhadap setiap parameter
4. *Update* parameter dengan bergerak kearah gradien negatif dengan
5. Ulangi proses sampai *konvergen* (loss tidak banyak berubah lagi).

$$
θ=θ−α⋅(∂L/∂θ)
$$

Dimana: 
- $θ$: Parameter (misalnya weight atau bias)
- $α$: Learning rate (ukuran langkah)
- $∂L/∂θ$: Turunan dari loss terhadap parameter

Contoh:
Kita punya sebuah DataShett yaitu: 

|   Berat Mobil (pounds)   |   Jarak Tempuh (Miles/Gallon)   |
|:---------------------:|:---------------------:|
|         3.5           |          18           |
|         3.69          |          15           |
|         3.44          |          18           |
|         3.43          |          16           |
|         4.34          |          15           |
|         4.42          |          14           |
|         2.37          |          24           |

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
Weight Slope: -119.7
$$
$$
Bias Slope: -34.3
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
Berbeda dengan parameter yang dihitung oleh model saat pelatihan, **hyperparameter** adalah variabel yang dapat dikendalikan. Tiga hyperparameter yang umum, yaitu:
1. Learning rate
2. Batch size
3. Epochs

### Learning Rate
**Learning rate** adalah nilai *float* yang dapat diatur untuk mempengaruhi kecepatan konvergensi suatu model. Jika learning rate suatu model terlalu rendah, konvergensi akan memakan waktu yang lama direnakan perubahan parameter terlalu kecil. Tetapi jika learning rate suatu model terlalu tinggi, parameter akan berubah terlalu besar dan menyebabkan fluktuasi yang mengakibatkan konvergensi tidak tercapai.

Learning rate yang ideal dapat membantu model untuk konvergensi dengan jumlah iterasi yang rasional. Maka dari itu tujuannya adalah untuk menentukan learning rate yang tidak terlalu tinggi atau terlalu rendah agar model dapat mencapai konvergensi dengan cepat. Berikut merupakan kurva *loss* dari contoh model yang berkembang secara signifikan di 20 iterasi awal sebelum berkonvergensi.

![Ideal Learning Rate](Image/Ideal-Learning-Rate.png)

### Batch Size
**Batch size** merujuk kepada jumlah data *example* yang diproses model sebelum memperbarui variabel *weights* dan *bias*. Dua teknik yang umum yaitu *stochastic gradient descent* and *mini-batch stochastic gradient descent*.

- ***Stochastic gradient descent* (SGD)**

Teknik ini hanya menggunakan satu *example* (ukuran *batch* adalah satu). Kata *"stochastic"* berarti *example* yang digunakan pada setiap *batch* terpilih secara acak. Teknik ini menghasilkan *noise* yang menyebabkan *loss* bertambah dibandingkan menurun seiring iterasi.

![Kurva SGD](Image/SGD-curve.png)

Dapat dilihat di kurva tersebut, model yang menggunakan *stochastic gradient descent* menghasilkan *noise* di seluruh kurva tidak hanya di dekat konvergensi.

- ***Mini-batch stochastic gradient descent* (mini-batch SGD)**

Untuk ***N*** jumlah poin data, *batch* akan berukuran lebih dari 1 dan kurang dari ***N***. Model memilih *examples*nya kedalam setiap batch secara acak, menghitung rata-rata gradien, lalu memperbarui *weights* dan *bias* sekali per iterasi.

![Kurva mini-batch SGD](Image/mini-batch-sgd.png)

Saat melatih model, beberapa *noise* dapat menjadi hal yang bermanfaat, terutama pada *neural network*.

### Epochs
**Epoch** artinya model telah memproses setiap *example* dalam pelatihan sebanyak sekali. Jumlah *epochs* merupakan hyperparameter yang perlu di tentukan sebelum pelatihan model dilaksanakan*

![Epochs Comparison Table](Image/Epochs.png)

## Logistic Regression

Logistic Regression adalah algoritma machine learning untuk klasifikasi biner. Tujuan utamanya adalah memperkirakan probabilitas dari suatu data masuk ke salah satu dari dua kelas (misalnya 0 atau 1, ya atau tidak).

> ### Model Logistic Regression
Model logistic regression mirip linear regression:

$$
z = w_1x_1 + w_2x_2 + .... + w_nx_n + b
$$

Namun, alih-alih langsung menggunakan z sebagai output, logistic regression menggunakan fungsi aktivasi sigmoid untuk mengubah nilai ini menjadi probabilitas antara 0 dan 1:

$$
\hat{y} = σ(z) = \frac{1}{1 + e^{-z}}
$$

### Langkah langkah Logistic Regression
1. Hitung ${z = wx + b}$

2. Hitung Probabilitas dengan Fungsi Sigmoid ${\hat{y} = \frac{1}{1 + e^{-z}}}$ 
3. Klasifikasi 
- Jika ${\hat{y} \geq 0.5}$ = Kelas 1
- Jika ${\hat{y} < 0.5}$ = Kelas 0

> ### Fungsi Loss: Log loss(Cross-Entropy)
Berbeda dengan linear regression yang memakai MSE, logistic regression menggunakan log loss:

$$
\text{Loss} = - \left[ y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y}) \right]
$$

- jika label ${y = 1}$ maka loss = ${-\text{Log}(\hat{y})}$
- jika label ${y = 0}$ maka loss = ${-\text{Log}(1 -\hat{y})}$

### Optimasi dengan Gradient Descent
Parameter \( w \) dan \( b \) diperbarui menggunakan **gradient descent**:

$$
w = w - \alpha \cdot \frac{\partial L}{\partial w}
$$

$$
b = b - \alpha \cdot \frac{\partial L}{\partial b}
$$

Di mana:
- $\alpha$: learning rate
- $\frac{\partial L}{\partial w}$:  turunan loss terhadap parameter

### Logistic vs Linear Regression
| Aspek            | Linear Regression       | Logistic Regression       |
|------------------|-------------------------|---------------------------|
| Output           | Nilai kontinu           | Probabilitas (0–1)        |
| Fungsi Aktivasi  | Tidak ada               | Sigmoid                   |
| Fungsi Loss      | Mean Squared Error      | Log Loss (Cross-Entropy)  |
| Tujuan           | Prediksi nilai kontinu  | Klasifikasi biner         |

## Klasifikasi *(Classification)*
Klasifikasi adalah proses memprediksi suatu objek atau data ke dalam kategori tertentu. Misalnya apakah email yang masuk itu merupakan *spam* atau bukan.

Dalam pembahasan klasifikasi, kita akan membahas berbagai topik penting seperti *thresholds* dan *confusion matrix*, akurasi (accuracy), presisi (precision), *recall*, serta *related metrics* lainnya. Selain itu, juga dibahas tentang ROC dan AUC, bias prediksi, dan pengenalan terhadap klasifikasi multikelas.

> ### Thresholds
Katakan jika kita mempunyai model regresi logistik untuk mengklasifikasikan apakah ini email *spam* atau bukan yang. Model ini memberikan nilai berupa 0 sampai 1, yang menunjukkan peluang apakah itu email *spam* atau bukan. Misal:
- 0.50 artinya 50% kemungkinan email itu spam.
- 0.75 artinya 75% kemungkinan spam, dan seterusnya.

Agar model ini bisa menyaring email secara otomatis perlu, kita perlu mengubah hasil angka tersebut menjadi kategori *spam* dan bukan *spam*. Disini *thresholds* dibutuhkan.

Thresholds merupakan nilai batas probabilitas. Jika hasil prediksi di atas threshold, maka email dikategorikan sebagai *spam*. Jika hasil prediksi di bawah threshold, maka dikategorikan sebagai bukan *spam*.

Misal suatu model mendeteksi satu email dengan skor 0.99 ( artinya 99% kemungkinan adalah spam) dan email lain dengan skor 0.51 (51% kemungkinan spam). Jika kita menetapkan nilai threshold sebesar 0.5 (50%), maka keduanya akan dianggap sebagai *spam*. Jika kita menaikkan nilai threshold sebesar 0.9 maka hanya email dengan skor 0.99 yang dianggap sebagai *spam*.

Apakah dengan menetapkan nilai threshold sebesar 0.5 adalah pilihan terbaik?. Jawabannya belum tentu karena ada beberapa faktor yang mempengaruhi di antaranya adalah:

1. Jumlah *spam* yang terlalu sedikit.
2. Kesalahan dalam memindahkan email penting ke folder spam lebih merugikan daripada membiarkan spam masuk ke inbox.

Dalam situasi seperti ini, menggunakan threshold di ambang batas 0.5 dapat memberikan banyak klasifikasi yang salah, dan membuat hasil akhir tidak sesuai harapan.

Jika kita telah menentukan nilai threshold yang kita rasa sudah tepat, penting juga untuk mengecek seberapa akurat model dalam mengklasifikasi data. Untuk itu, kita dapat menggunakan yang namanya *confusion matrix*.

> ### Confusion Matrix

Confusion matrix merupakan sebuah tabel yang digunakan untuk mengevaluasi performa model klasifikasi. Tabel ini membandingkan prediksi model dengan kenyataan sebenarnya (*ground truth*) dan menunjukkan seberapa sering model membuat prediksi yang benar maupun salah. Terdapat 4 kemungkinan hasil dalam confusion matrix, yaitu:
|                         | Actual Positive (Spam) | Actual Negative (Bukan Spam) |
|-------------------------|---------------------------|----------------------------------|
| **Prediction: Positive**   | True Positive (TP)         | False Positive (FP)              |
| **Prediction: Negative**   | False Negative (FN)        | True Negative (TN)               |
-------------------------------------------------------------------------------------------

**Penjelasan Confusion Matrix: TP, FP, FN, TN**

| Singkatan | Nama Lengkap         | Arti Prediksi                                                                 | Contoh                                                                               |
|-----------|----------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **TP**    | True Positive         | Model **benar** memprediksi data sebagai **positif**                         | Email **spam** yang diprediksi sebagai **spam**                                      |
| **FP**    | False Positive        | Model **salah** memprediksi data sebagai **positif**, padahal sebenarnya **negatif** | Email **bukan spam** yang diprediksi sebagai **spam** (*false alarm*)               |
| **FN**    | False Negative        | Model **salah** memprediksi data sebagai **negatif**, padahal sebenarnya **positif** | Email **spam** yang diprediksi sebagai **bukan spam** (*missed detection*)          |
| **TN**    | True Negative         | Model **benar** memprediksi data sebagai **negatif**                         | Email **bukan spam** yang diprediksi sebagai **bukan spam**                          |

> ### Accuracy, recall, precision, dan Metrik Lainnya
### Accuracy (Akurasi)
Akurasi merupakan  proporsi seberapa banyak prediksi model yang benar, baik tebakan yang positif (*spam*) maupun negatif (bukan *spam*). Untuk menghitung akurasi pada model dapat dihitung dengan formula sebagai berikut:

$$
\text{Accuracy} = \frac{\text{correct classifications}}{\text{total classifications}} = \frac{TP + TN}{TP + TN + FP + FN}
$$

Akurasi cocok digunakan kalau data antara kelas positif dan negatif jumlahnya seimbang. Jika data tidak seimbang akurasi yang didapatkan kurang baik.

### Recall (True Positive Rate)
Recall merupakan proporsi dari tebakan positif yang benar (TP) dengan semua tebakan positif (Actual Positive). Dengan rumus sebagai berikut:

$$
\text{Recall} = \frac{\text{correctly classified actual positives}}{\text{all actual postives}} = \frac{TP}{TP + FN}
$$

Recall merupakan ukuran seberapa baik sebuah model dalam mengenali semua data yang termasuk kategori positif. Metode ini penting dalam situasi di mana melewatkan satu data penting saja dapat memberikan dampak yang besar. Recall cocok digunakan dengan data yang tidak seimbang, dimana jumlah kasus positif jauh lebih sedikit dibandingkan kasus negatif. Dalam kondisi seperti ini, akurasi bisa saja memberikan informasi yang salah karena model mungkin tampak **baik** secara angka, padahal sebenarnya banyak data penting yang tidak terdeteksi.

### False Positive Rate (FPR)
False Positive Rate (FPR) merupakan proporsi dari tebakan positif yang salah (FP) dengan semua tebakan negatif baik yang benar maupun salah (Actual Negative). Dirumuskan sebagai berikut:

$$
\text{FPR} = \frac{\text{incorrectyly classified actual negatives}}{\text{all actual negatives}} = \frac{FP}{FP + TN}
$$

FPR menunjukkan seberapa sering model salah menandai data yang seharusnya negatif sebagai positif. Cocok digunakan jika jumlah data negatif cukup banyak, tetapi tidak terlalu berguna saat data negatif sangat sedikit.

### Precision (Presisi)
Precision adalah proporsi dari tebakan positif yang benar (TP) dengan semua yang diklasifikasikan sebagai positif (Actual Positive). Dirumuskan sebagai berikut:

$$
\text{TPR} = \frac{\text{correctly classified actual positives}}{\text{everything classified as positive}} = \frac{TP}{TP + FN}
$$

Precision sangat berguna untuk mengetahui seberapa akurat prediksi positif yang dibuat model. Tapi pada kondisi tertentu, terutama saat data tidak seimbang, precision harus digunakan bersama metrik lain seperti recall untuk mendapatkan gambaran performa model yang lebih tepat.

#### **Saran Pemilihan Metrik**
| **Metrik**              | **Panduan Penggunaan**                                                                 |
|-------------------------|----------------------------------------------------------------------------------------|
| **Akurasi**             | - Gunakan sebagai indikator kasar untuk memantau proses pelatihan model pada data seimbang.  |
|                         | - Untuk menilai performa model, gunakan bersama metrik lain.                          |
|                         | - Hindari pada dataset yang tidak seimbang. Pertimbangkan metrik lain.                |
| **Recall (True positive rate)** | Gunakan ketika kesalahan false negative lebih berdampak daripada false positive.       |
| **False positive rate** | Gunakan ketika kesalahan false positive lebih berdampak daripada false negative.      |
| **Presisi**             | Gunakan ketika sangat penting bahwa prediksi positif benar-benar akurat.              |

> ### ROC dan AUC

### Kurva ROC (Receiver Operating Characteristic)

Kurva ROC merupakan representasi visual dari pefroma model dari semua threshold. Kurva ROC diplot berdasarkan nilai dari true positive rate (TPR) dan false positive rate (FPR). Model yang baik adalah model yang memiliki nilai TPR sebesar 1.0 dan FPR sebesar 0.0

![ROC](Image/ROC.png)

Gambar di atas menunjukkan grafik Receiver Operating Characteristic (ROC) dari sebuah model klasifikasi. Sumbu horizontal merepresentasikan False Positive Rate (FPR), yaitu proporsi data negatif yang salah diklasifikasikan sebagai positif. Sementara itu, sumbu vertikal menunjukkan True Positive Rate (TPR), yaitu proporsi data positif yang berhasil diklasifikasikan dengan benar.

Pada grafik ini, kurva ROC membentuk garis horizontal di posisi TPR = 1.0 yang membentang dari FPR = 0.0 hingga FPR = 1.0. Ini menunjukkan bahwa model mampu mengenali seluruh data positif dengan benar di seluruh nilai ambang klasifikasi. Pada threshold tertentu, model bahkan dapat memisahkan data positif dan negatif secara sempurna tanpa membuat kesalahan klasifikasi, yang ditunjukkan oleh titik (FPR = 0, TPR = 1) pada kurva.

### Area Under the Curve (AUC)

Area Under the Curve merupakan ukuran seberapa baik model klasifikasi dapat membedakan antara dua kelas (misalnya, positif dan negatif). Nilainya berkisar antara 0 dan 1. Model yang sempurna memiliki AUC sebesar 1,0, artinya model selalu bisa membedakan data positif dan negatif dengan benar. Secara sederhana, AUC menunjukkan peluang 100% bahwa model akan memberi skor lebih tinggi pada data positif dibanding data negatif, tanpa tergantung pada ambang batas yang dipilih.

AUC berguna untuk membandingkan performa dua model, terutama jika dataset cukup seimbang. Model dengan AUC lebih besar umumnya memiliki performa yang lebih baik. Titik-titik pada kurva ROC yang paling dekat dengan titik (0,1) menunjukkan threshold terbaik bagi model tersebut. Namun, pemilihan threshold tergantung pada metrik yang paling penting sesuai kebutuhan kasus penggunaan, seperti dibahas dalam bagian confusion matrix dan metrik lainnya.

### Prediction Bias

Prediksi Bias adalah selisih antara rata rata (*Mean*) dan Prediksi model, dan rata rata dari Label Sebenarnya(actual) daalam data. 
Tujuan dari prediksi bias ini adalah menjadi idikator cepat untuk mendeteksi apakah model representatif dengan data, dan apakah ada masalah dalam data.
Contoh:
Jika 5% dari semua email dalam dataset adalah spam (label mean = 0.05), maka:
- Model yang baik seharusnya juga memprediksi sekitar 5% sebagai spam.
- Jika model malah memprediksi 50% email sebagai spam (prediction mean = 0.5), berarti ada masalah serius.

**Penyebab Prediction bias:**
1. Data Bermasalah 
  - contoh: Sampling data training tidak seimbang.
2. Regularisasi terlalu kuat
  - contoh: Model terlalu sederhana dan gagal menangkap pola penting.
3. Bug dalam pipeline training
  - Kesalahan saat preprocessing.
4. Fitur tidak memadai
  - Model tidak punya cukup informasi untuk membuat prediksi akurat.

> ### Multi Class classification

Multi-class classification adalah perpanjangan dari binary classification di mana:
- Setiap data hanya boleh memiliki satu kelas dari beberapa kelas yang tersedia.
- Contoh umum: klasifikasi angka tulisan tangan dari 0 sampai 9.

Multi-class dapat diselesaikan dengan beberapa binary classifier. Salah satu pendekatan disebut **One-Vs-Rest (OVR)**.
contoh:
- Model 1: A + B vs C
- Model 2: A vs B
- Dari kombinasi diatas akan menghasilkan pemisahan akhir antara A, B dan C.

**Perbedaan Multi-class dan Label Multi-label**
| Aspek                   | Multi-Class                        | Multi-Label                                  |
| ----------------------- | ---------------------------------- | -------------------------------------------- |
| Jumlah label per contoh | Satu label                         | Satu atau lebih label                        |
| Output model            | Probabilitas per kelas, pilih satu | Probabilitas per kelas, bisa lebih dari satu |
| Contoh                  | Klasifikasi angka 0–9              | Gambar berisi anjing dan kucing              |

<br>

## **2. Data**
Data merupakan bagian yang penting di Machine Learning. Evaluasi, transformasi, *cleaning* merupakan perlakuan data yang diperlukan agar suatu model Machine Learning memiliki performa yang lebih baik.

## Numerical Data
***Numerical data*** atau data numerik adalah data angka integer atau float yang dapat dijumlahkan, dihitung, diurutkan, dibandingkan dan lain sebagainya.

> ### Feature Vectors
***Feature vector*** adalah array nilai fitur yang terdiri dari *example*, diinputkan selama pelatihan dan selama inferensi. Untuk menghasilkan model yang bagus, nilai data asli perlu diubah agar dapat lebih efisien untuk pelatihan. Proses ini dinamakan *Feature engineering*, dengan dua teknik umumnya yaitu:
1. Normalisasi
2. *Binning*

> ### Visualisasi data
Sebelum memasuki ke analasis, mari kita visualisasi data terlebih dahulu. Dengan memvisualisasi data, kita dapat menemukan pola tersembunya dalam data. [Pandas](https://pandas.pydata.org/) merupakan *software library* yang dirancang untuk memanipulasi dan menganalisis data. Kami rekomendasi menggunakan [pandas](https://pandas.pydata.org/) untuk visualisasi.
- [Working with Missing Data (pandas Documentation)](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)
- [Visualizations (pandas Documentation)](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

> ### Normalization
**Normalisasi** merupakan proses pengubahan nilai aktual fitur menjadi nilai dengan skala yang sama untuk pelatihan model yang lebih efisien. Normalisasi dapat membantu model konvergensi lebih cepat, menyimpulkan prediksi lebih baik, menghindari *"NaN Trap"* saat nilai fitur sangat tinggi, dan mempelajari *weights* untuk setiap fitur.

> *Catatan: Fitur yang dinormalisasi saat latihan perlu dinormalisasi juga jika melakukan prediksi*

Tiga metode normalisasi yang akan kita bahas yaitu:
- Linear scaling
- Z-score scaling
- Log scaling

### Linear Scaling
***Linear scaling*** berarti mengkonversikan nilai floatin point dari rentang alaminya menjadi rentang standar.

**Cara menghitung Linear Scaling**

Rumus untuk mengskalakan ke rentang standar 0 hingga 1, inklusif:

$$
x'=(x-x_{min})/(x_{max}-x_{min})
$$

Keterangan:
- ${x'}$ adalah nilai yang diskalaka.
- ${x}$ adalah nilai asli.
- $x_{min}$ adalah nilai terendah di dataset fitur ini.
- $x_{max}$ adalah nilai tertinggi di dataset fitur ini.

*Linear scaling* menjadi opsi yang bagus ketika batas data tidak berubah sewaktu-waktu, fitur memiliki sedikit atau tidak memiliki outlier yang tidak ekstrem, fitur terdistribusi secara merata diseluruh rentangnya.

### Z-Score Scaling
Metode normalisasi ***Z-Score Scaling*** adalah jumlah simpangan baku nilai dari rata-rata. Merujuk ke gambar berikut sebagai contoh.

![Z-Score Classic](./Image/z-scaling_classic.png)
Data mentah (kiri) dan *Z-Score Scaling* (kanan) untuk distribusi normal.

![Z-Score non-Classic](./Image/z-scaling-non-classic-normal-distribution.png)
Data mentah (kiri) dan *Z-Score Scaling* (kanan) untuk distribusi normal non-klasik.

**Cara menghitung *Z-Score Scaling***

$$
x'=(x-μ)/σ
$$

Keterangan:
- ${x'}$ adalah Z-Score.
- ${x}$ adalah nilai mentah; Nilai yang akan dinormalisasi.
- ${μ}$ adalah mean.
- ${σ}$ adalah standar deviansi.

Z-score merupakan opsi yang bagus ketika data mengikuti distribusi normal atau distribusi yang mirip seperti distribusi normal.

### Log Scaling
***Log scaling*** menghitung logaritma nilai rendah. Logaritma dapat berbasis apa pun, biasanya *log scaling* menghitung logaritma natural (ln).

**Cara menghitung Log Scaling**

$$
x'=ln(x)
$$

Keterangan:
- ${x'}$ adalah logaritma alami ${x}$
- Nilai asli = 54.598

Log scaling berguna jika data sesuai dengan distribusi *hukum pangkat*. Secara umum, *hukum pangkat* adalah sebagai berikut:
- Nilai x yang rendah memiliki nilai Y yang sangat tinggi.
- Seiring meningkatnya nilai X, nilai Y akan menurun. Akibatnya, nilai tinggi X memiliki nilai Y yang sangat rendah.

![Movie Rating Comparison Log Scaling](./Image\log-scaling-movie-ratings.svg)
Contoh perbandingan distribusi mentah dengan lognya.

### Clipping

if ${x>max}$, set ${x'=max}$

if ${x<min}$, set ${x'=min}$

***Clipping*** atau pemangkasan adalah metode untuk meminimalisir pengaruh *outliers* ekstrem. Secara singkat, clipping mengurangi nilai dari *outliers* ke nilai maksimum spesifik.

![Clipping example](./Image/clipping-example.png)

Dari histogram tersebut, dapat dilihat bahwa fitur di clipping di nilai 4.0. Hal ini bukan berarti model mengabaikan semua nilai diatas 4.0, tetapi nilai tersebut menjadi 4.0. Clipping juga bisa digunakan setelah dilakukan normalisasi seperti clipping normalisasi Z-Score, Log, dan sebagainya. Clipping mencegah model *overindexing* data tidak penting, tetapi beberapa *outliers* sebenarnya penting, maka dari itu diperlukan keterletian lebih untuk clipping.

> ### Binning
***Binning*** (atau *bucket*) merupakan teknik yang mengelompokkan berbeda *numerical subranges* kedalam kelompok atau *bin*. Binning juga dapat digunakan untuk mengubah *numerical data* menjadi *categorical data*.

Contoh binning:
| No. Bin | Rentang |     *Feature Vector*      |
|:-------:|:-------:|:-------------------------:|
|    1    |  15-34  | [1.0, 0.0, 0.0, 0.0, 0.0] |
|    2    |  35-117 | [0.0, 1.0, 0.0, 0.0, 0.0] |
|    3    | 118-279 | [0.0, 0.0, 1.0, 0.0, 0.0] |
|    4    | 280-392 | [0.0, 0.0, 0.0, 1.0, 0.0] |
|    5    | 393-425 | [0.0, 0.0, 0.0, 0.0, 1.0] |

Binning adalah alternatif *scaling* atau *clipping* jika ada kondisi berikut:
- Keseluruhan hubungan *linear* antara fitur dan label lemah atau tidak ada.
- Saat nilai fitur dikelompokkan.

### Quantile Bucketing
***Quantile Bucketing*** membuat batas pengelompokkan sehingga jumlah *example* di setiap bucket sama persis atau hampir sama.

![Quantile bucketing](./Image/quantile-bucketing.png)

Visualisasi tersebut menggunakan *quantile bucketing* untuk mendistribusi harga mobil dengan jumlah *example* yang sekiranya sama di setiap *bucket*.

> ### Scrubbing
Data *Scrubbing* atau lebih dikenal sebagai Data *Cleaning* dilakukan untuk mengidentifikasi masalah, inkonsistensi, ketidakakuratan dalam dataset dan mengoreksinya. Banyak *example* di *dataset* yang tidak dapat di andalkan karena beberapa hal.

|       Kategori Masalah       |                    Contoh                     |
|:----------------------------:|:---------------------------------------------:|
| Nilai yang tidak ditampilkan | Peserta gagal mencatat usia seorang penduduk  |
| *example* ganda              | Server mengupload log yang sama               |
| Nilai fitur di luar rentang  | Manusia tidak sengaja mengetik digit tambahan |
| Label buruk                  | Evaluator manusia salah melabeli tanaman      |

Untuk tiga label pertama dapat dibuatkan program atau skrip untuk mendeteksi salah satu masalah tersebut. Misalnya jika rentang suhu untuk rentang tertentu mendapati *outlier* buruk, program diperlukan untuk mengidentifikasi nilai suhu yang melebihi nilai spesifik untuk dibersihkan.

### Fitur numerik yang berkualitas

***Clearly Named***

Setiap fitur harus memiliki makna yang jelas dan masuk akal untuk manusia di proyek tersebut. Contohnya:

| Tidak jelas |   Jelas  |
|-------------|----------|
| <pre>Umur: 961</pre> | <pre>Umur: 27</pre> |

*Tidak masuk akal.*

**Diperiksa atau diuji sebelum *testing***

Dalam beberapa kasus, data buruk dapat diakibatkan nilai yang tidak jelas. Beberapa dapat juga berasal dari sumber yang tidak diperiksa terlebih dahulu.

| Data salah | Data benar |
|------------|------------|
| <pre>Umur: 227</pre> | <pre>Umur: 27</pre> |

*Nilai di data yang tidak diperiksa, kemungkinan data yang dimaksud adalah 27.*

***Sensible***

*"Magic Value"* adalah diskontinuitas yang disengaja dalam fitur berkelanjutan. Misal sebuah fitur kontinu yang dapat menyimpan nilai float,

<pre>watch_time_in_seconds: -1</pre>

Karena nilai data tersebut -1, model akan mencari tahu dan akan menonton film ke belakang. Hal tersebut tidak masuk akal secara logika dan prediksi yang dihasilkan tidak akan bagus.

<pre>watch_time_in_seconds: 4.82
watch_time_in_seconds_defined=True

watch_time_in_seconds: 0
watch_time_in_seconds_defined=False</pre>

Dalam kasus ini, dengan menandakan nilai data yang hilang menggunakan nilai baru, model akan mempelajari *weights* yang berbeda untuk setiap nilai.

> ### Polynomial Transforms

Disaat suatu baribel terkait dengan kuadrat, kubik, atau pangkat lain dari variabel lain, lebih baik membuat *synthetic feature* dari salah satu *numerical feature* yang ada. *Synthetic feature* sendiri berarti fitur yang tidak ada dari fitur input, tetapi terancang dari satu dan banyak lainnya fitur.

![Polynomial](./Image/Polynomial-example.png)

Di contoh visualisasi tersebut, lingkaran pink dan segitiga hijau merepresentasikan kategori yang berbeda. Dari visualisasi yang didapatkan, tidak memungkinkan untuk membuat garis lurus untuk memisahkan kedua kategori, tapi dapat dibuat kurva ${y=x^2}$ untuk memisahkannya.

Seperti yang telah dibahas sebelumnya, model linear dengan satu fitur dapat menggunakan

$$
y=b+w_1x_1
$$

Gradien descent dapat meminimalisir *loss* suatu model, tetapi karena tidak dapat dibuat garis lurus, maka dapat kita definisikan

$$
x_2=x_1^2
$$

*Synthetic feature* ini, disebut polynomial transform, dianggap seperti fitur lainnnya. Rumus linear sebelumnya menjadi

$$
y=b++w_1x_1+w_2x_2
$$

Dengan pengaplikasian ini, menjadi mungkin untuk memisahkan kedua kategori data tanpa mengubah cara belajar model linear menggunakan ${y=b++w_1x_1+w_2x_2}$, walaupun adanya kuadrat tersembunyi.

### Kesimpulan
Kondisi model Machine Learning ditentukan oleh datanya. Data yang baik akan mengembangkannya dan yang buruk akan membuat prediksinya buruk.

Praktik terbaik untuk bekerja dengan numerical data:
- Model ML berinteraksi dengan data di *feature vector*, bukan di dataset.
- Normasilasis sebagian besar fitur numerik.
- Petimbangkan metode normalisasi yang lain jika metode normalisasi pertama gagal.
- Binning (atau *bucketing*) terkadang lebih baik dibandingkan normalisasi.
- Pertimbangkan bagaimana seharusnya data tersebut, tulis tes verifikasi untuk memvalidasi ekspetasi tersebut.
- Visualisasi data dengan scatter plot dan histogram, cari anomali.
- Kumpulkan statistik dari seluruh dataset dan juga dari *subset* yang lebih kecil dari dataset tersebut.
- Dokumentasi semua transformasi data.

## Categorical Data

### Data Kategorik vs Data Numerik

**Data Kategorik**

- Data kategorik adalah data yang terdiri dari kategori atau label yang **tidak memiliki hubungan numerik** yang jelas.
- Contoh: Warna lampu lalu lintas (*red*, *yellow*, *green*), jenis kelamin (*male*, *female*).
- Data kategorik **diindeks** dan diterjemahkan ke dalam format numerik agar bisa digunakan dalam model machine learning (ML).

**Data Numerik**

- Data numerik adalah data yang terdiri dari **angka**, baik bilangan bulat (integer) atau angka desimal (*real-number*).
- Contoh: Ukuran rumah dalam meter persegi, harga produk.
- Data numerik memiliki hubungan matematis yang bisa dihitung, seperti penjumlahan dan pengurangan.

> ### Encoding: Mengonversi Data Kategorik menjadi Vektor Numerik

**Nomor Indeks**

- Data kategorik diubah menjadi **nomor indeks** unik.
- **Masalah**: Jika data kategorik hanya diubah menjadi angka, model bisa menganggap angka tersebut sebagai data numerik (misalnya, *red* = 0, *green* = 1, *yellow* = 2) yang menghasilkan hubungan yang tidak tepat (misalnya, model akan menganggap *yellow* lebih besar daripada *red*).
- **Solusi**: Gunakan one-hot encoding untuk menghindari hal ini.

**One-Hot Encoding**

- Mengonversi kategori menjadi vektor **binary** dengan panjang sama dengan jumlah kategori yang ada.
- **Contoh**:

  * Kategori: *red*, *yellow*, *green*
  * One-Hot Encoding:
    * red = \[1, 0, 0]
    * yellow = \[0, 1, 0]
    * green = \[0, 0, 1]
* **Kelebihan**: Tidak ada hubungan numerik yang keliru, cocok untuk kategori yang tidak memiliki urutan.
* **Catatan**: Sering kali menghasilkan vektor yang sangat panjang jika jumlah kategori besar (dimensi tinggi).

**Multi-Hot Encoding**

* **Multi-Hot Encoding** memungkinkan lebih dari satu nilai 1 di dalam vektor, digunakan ketika data kategorik bisa memiliki lebih dari satu nilai.
* **Contoh**: Genre film *Action*, *Comedy*, dan *Drama*.

  * Jika film memiliki dua genre *Action* dan *Comedy*, vektor multi-hot-nya bisa begini bentuknya: `[1, 1, 0]`.
* **Masalah**: Menghasilkan vektor yang lebih jarang dan memakan lebih banyak ruang memori jika jumlah kategori besar.

### Dimensi Tinggi dan Pengurangan Dimensi

- **Dimensi tinggi** terjadi ketika kita memiliki banyak kategori dalam data kategorik, yang menghasilkan vektor fitur dengan banyak elemen.
- **Masalah**: Dimensi tinggi meningkatkan **biaya pelatihan** dan mempersulit model untuk belajar.
- **Solusi**: Gunakan **embedding** atau **hashing** untuk mengurangi dimensi dan meningkatkan efisiensi model.

> ### Embedding dan Hashing untuk Mengurangi Dimensi Tinggi

**Embedding**

- Embedding digunakan untuk mengonversi data kategorik berdimensi tinggi menjadi vektor **padat** dengan dimensi yang lebih kecil.
- **Contoh**: Mengonversi kata-kata seperti "dog", "cat", "fish" menjadi vektor berdimensi rendah yang memiliki makna lebih dekat secara semantik.
- **Kelebihan**: Mengurangi dimensi, mempercepat pelatihan, dan meningkatkan akurasi model.

**Hashing**

- **Hashing** adalah cara lain untuk mengurangi dimensi dengan menggunakan fungsi hash untuk mengonversi kategori menjadi ID numerik lebih kecil.
- **Contoh**: Menggunakan fungsi hash untuk menghasilkan ID untuk kategori seperti "apple" menjadi 5, "banana" menjadi 9, "pear" menjadi 5 juga.
- **Kekurangan**: Dapat menyebabkan **tabrakan (collision)**, di mana dua kategori berbeda mendapatkan ID yang sama, yang bisa mengurangi akurasi model.

> ### Fitur Silang (Feature Crossing)

**Apa Itu Fitur Silang?**

- **Fitur silang (*Feature Crossing*)** adalah teknik untuk **menggabungkan dua atau lebih fitur kategorik** untuk menciptakan fitur baru yang menangkap **interaksi antar fitur**.
- Misalnya, menggabungkan fitur *edges* (smooth, toothed, lobed) dan *arrangement* (opposite, alternate) untuk menghasilkan kombinasi:

  * Smooth\_Opposite
  * Smooth\_Alternate
  * Toothed\_Opposite
  * Toothed\_Alternate
  * Lobed\_Opposite
  * Lobed\_Alternate
- Fitur silang memungkinkan model untuk **menangani non-linearitas** dalam data.

**Kapan Menggunakan Fitur Silang?**

- Digunakan ketika kita ingin menangkap **interaksi antar fitur** yang tidak bisa dipelajari hanya dengan fitur individual.
- **Contoh**: Memahami pengaruh interaksi antara *jenis kelamin* dan *umur* terhadap preferensi produk.

**Risiko Fitur Silang:**

- **Fitur jarang (*Sparse Feature*)**: Menyilangkan dua fitur jarang menghasilkan fitur baru yang lebih jarang dan **lebih sulit dipelajari** oleh model.
- **Contoh**: Menyilangkan dua fitur jarang, seperti *kode pos* dan *warna*, bisa menghasilkan ribuan kombinasi yang jarang muncul, sehingga model kesulitan belajar.

> ### Pentingnya Kualitas Data: Pelabelan Manusia vs Mesin

**Pelabelan Manual (Label Emas)**

- Data yang diberi label oleh manusia sering dianggap lebih akurat dan dapat dipercaya, namun masih bisa mengandung **kesalahan manusia, bias**, atau **niat jahat**.
- **Kesepakatan antar penilai**: Mengukur seberapa konsisten label yang diberikan oleh beberapa penilai manusia untuk contoh yang sama.

**Pelabelan Mesin (Label Perak)**

- Data yang diberi label secara otomatis oleh model klasifikasi atau algoritma machine learning.
- Kualitas bisa sangat bervariasi, dan model bisa menghasilkan **kesalahan** atau **bias** tertentu jika dilatih dengan data yang tidak akurat.

## Datasets, Generalization, dan Overfitting

Dataset adalah kumpulan contoh data yang biasanya disimpan dalam bentuk tabel seperti CSV, spreadsheet, atau database. Setiap baris mewakili satu contoh (sample), dan setiap kolom menunjukkan fitur (fitur input) atau label (output yang diprediksi).

> ### Jenis-jenis Data
- Numerical Data (angka).
- Categorical Data (kelas atau kategori).
- Human Language (kata, kalimat, dokumen).
- Multimedia (gambar, video, audio).
- Output dari sistem ML.
- Embeddings vectors (representasi numerik dari data kompleks).

> ### Jumlah Data
Jumlah dataset harus lebih banyak (minimal 10-100 kali lipat) dibanding jumlah parameter model yang dilatih.
- Model sederhana + data banyak = hasil bagus.
- Model kompleks + data sedikit = cenderung kurang efektif.
- Transfer learning memungkinkan hasil bagus dengan data kecil, jika model sebelumnya sudah dilatih pada data yang relevan dan besar.

> ### Kualitas dan Keandalan Data

Data yang berkualitas tinggi dapat membantu model mencapai tujuannya, sedangkan data berkualitas rendah dapat menghambat kinerja model.

Keandalan pada data harus dipengaruhi oleh beberapa faktor sebagai berikut:
- Kesalahan label
- Fitur yang tidak akurat (*Noisy Features*)
- Relevansi Data

Penyebab data tidak andal di antara lain:
- Nilai yang hilang
- Data terduplikat
- Nilai fitur yang salah
- Label yang salah
- Bagian data yang buruk

> ### Labels

Labels adalah nilai atau jawaban yang ingin diprediksi oleh model. Labels biasanya adalah output dari data yang telah diketahui, dan digunakan untuk melatih model agar bisa memprediksi hal yang sama terhadap data baru. Dalam pembahasan kali ini akan menjelaskan **direct labels** dan **proxy labels**.

1. Direct labels merupakan label yang identik dengan apa yang ingin diprediksi oleh model. Contoh jika ingin mengklasifikasikan kepemilikan kendaraan maka kita dapat membuat label sebagai pemilik_kendaraan.

2. Proxy labels merupakan label yang mirip atau berkaittan dengan prediksi yang diinginkan, tetapi tidak identik. Contoh kita membuat kolom bernama penyewa_majalah_kendaraan, label ini hanya mengindikasikan kemungkinan seseorang memiliki kendaraan.

#### Kesimpulan: Direct Labels vs Proxy Labels

- **Direct labels** lebih disarankan karena memberikan data yang **langsung sesuai** dengan prediksi yang ingin dibuat oleh model. Hal ini menghasilkan pelatihan yang lebih akurat dan model yang lebih andal.

- **Proxy labels** digunakan sebagai **alternatif** jika direct label tidak tersedia atau tidak bisa digunakan secara teknis (misalnya: tidak bisa direpresentasikan dalam bentuk numerik).

- Penggunaan **proxy label adalah kompromi**, dan efektivitas model sangat bergantung pada **seberapa kuat hubungan** antara proxy label dan target prediksi yang sebenarnya.

- Dalam pengembangan model machine learning, **selalu prioritaskan label yang eksplisit, relevan, dan representatif**. Gunakan proxy label hanya jika diperlukan, dengan **kehati-hatian dan pemahaman terhadap keterbatasannya**.

> ### Human Generated Data

Human-generated data adalah data yang nilai atau labelnya ditentukan oleh manusia melalui pengamatan atau penilaian. Contohnya, seorang meteorolog bisa melihat foto langit dan menentukan jenis awan di dalamnya.

Sebaliknya, ada juga data yang automatically-generated, yaitu nilai atau label ditentukan oleh sistem otomatis seperti model machine learning lain.

#### Keuntungan Menggunakan Human Generated Data
- Fleksibilitas tinggi: Penilai manusia dapat menyelesaikan berbagai tugas kompleks yang bahkan sulit untuk model ML.
- Standarisasi proses: Melibatkan manusia memaksa pemilik dataset untuk menetapkan kriteria yang jelas dan konsisten, meningkatkan kualitas pelabelan.

#### Kerugian Menggunakan Human Generated Data
- Biaya tinggi: Karena melibatkan manusia, proses ini biasanya membutuhkan bayaran, sehingga lebih mahal dibanding otomatisasi.
- Kesalahan manusiawi: Manusia bisa salah menilai, sehingga seringkali dibutuhkan beberapa penilai untuk satu data demi meningkatkan akurasi.

Data yang dihasilkan manusia bisa sangat bernilai karena kemampuannya menangani tugas kompleks yang sulit untuk otomatisasi. Namun, biayanya yang tinggi dan risiko kesalahan perlu dipertimbangkan secara serius. Keputusan untuk menggunakan data ini harus mempertimbangkan kebutuhan kualitas, waktu, dan sumber daya yang tersedia.

> ### Imbalanced Datasets

Jika ada data positif atau negatif seimbang maka dapat disebut sebagai dataset yang seimbang atau *balanced datasets*. Jika ada satu label saja yang lebih dominan maka disebut  dataset yang tidak seimbangan atau *imbalanced datasets*. Label yang dominan dalam dataset yang tidak seimbang disebut ***majority class***, sedangkan label yang kurang dominan disebut sebagai ***minority class***.

Tabel berikut ini menjelaskan kategori tingkat ketidakseimbangan berdasarkan persentase data yang termasuk ke dalam minority class:
| Persentase Minority Class | Derajat Imbalance |
| ------------------------- | ----------------- |
| 20-40%                    | Mild              |
| 1-20%                     | Moderate          |
| < 1%                      | Extreme           |

Sebagai contoh pada dataset pendeteksi virus. Minority class direpresentasikan sebesar 0.5% dari dataset yang ada dan majority class sebesar 99.5%. Dataset yang seperti ini sangat umum di dunia medis dikarenakan subjek tidak selalu memiliki virus di dalamnya.

![Imbalanced-datasets](./Image/Imbalanced%20Datasets.png)

Dataset yang tidak seimbang tidak memiliki cukup contoh minority class
untuk melatih model dengan baik. Karena hanya memiliki sedikit label positif, model dilatih dengan menggunakan label negatif dan tidak dapat mempelajari label positif dengan cukup. Sebagai contoh jika ukuran batch sebesar 50, mungkin banyak batch tersebut tidak mengandung label positif.

Untuk midly imbalanced dan moderately imbalanced datasets, ketidakseimbangan dataset tidak masalah. Maka dari itu, cobalah untuk melatih model dengan dataset asli. Jika model bekerja dengan baik maka pekerjaan sudah selesai. Jika belum, model yang belum optimal tersebut dapat menjadi landasan untuk eksperimen ke depannya. Ada beberapa teknik yang dapat digunakan untuk mengatasi ketidakseimbangan dataset yaitu dengan Downsampling dan Upweighting.

#### **Downsampling dan Upweighting**

- Downsampling artinya mengurangi jumlah data dari kelas yang dominan agar lebih seimbang dengan jumlah data dari kelas yang kurang dominan. Sebagai contoh apabila kita mempunyai 1000 data berlabel negatif dan 100 data berlabel positif. Model akan cenderung **"mengabaikan"** data positif karena terlalu banyak data negatif. Dengan downsampling, data yang di ambil adalah sebagian kecil dari data negatif, misalnya hanya 100 data negatif. Jadi model akan dilatih dengan menggunakan 100 data negatif dan 100 data positif.

- Upweighting merupakan teknik yang digunakan untuk memberi bobot lebih besar dari kelas minoritas, agar model lebih **memperhatikan** data tersebut ssat dilatih. Namun dalam konteks downsampling, upweighting justru dilakukan pada kelas mayoritas yang sudah dikurangi jumlahnya agar tetap sebanding. Contohnya jika ada 1000 data negatif dan 100 data positif lalu downsampling kelas negatif menjadi 100 data negatif. Agar model tetap menganggap 100 data negatif mewakili 1000 data aslinya, setiap data negatif diberi bobot 10x lebih berat (karena 1000: 100 =10)

*Weight* yang dimaksud disini bukan seperti (w1 atau w2). *Weight* disini mereferensikan sebagai *example weights*, yang dimana seberapa penting suatu data dianggap oleh model saat proses pelatihan. Sebagai contoh apabila sebuah data diberi **example weights = 10**, artinya model menganggap data tersebut 10 kali lebih penting dibandingkan data dengan weight = 1 (saat menghitung loss).

*Weight* seharusnya sama dengan faktor yang digunakn untuk downsampling:

$$
\text{example weight} = \text{original example weight} * \text{downsampling factor}
$$

Pemberian bobot lebih pada kelas mayoritas berguna untuk mengurangi bias prediksi. Hal ini membantu untuk menjaga nilai rata-rata prediksi model agar tetap mendekati rata-rata label di dataset asli.

#### Rebalance Ratios

Untuk menentukan seberapa besar downsampling dan upweighting yang diperlukan untuk menyeimbangkan dataset, jawabannya perlu ditemukan melalui eksperimen.Ada beberapa faktor yang mempengaruhi:
- Ukuran batch
- Rasio ketidakseimbangan
-  Jumlah total data pada training set

Idealnya, setiap batch harus berisi beberapa contoh dari kelas minoritas. Jika sebuah batch tidak mengandung cukup data dari kelas minoritas, proses pelatihan model akan berjalan sangat buruk. Oleh karena itu, ukuran batch sebaiknya beberapa kali lebih besar dari rasio ketidakseimbangan.
Misalnya, jika rasio ketidakseimbangan adalah 100:1, maka ukuran batch minimal yang disarankan adalah 500.

### Pembagian Dataset Asli

#### Training, Validation, and Test Sets

1. **Training Set** digunakan model untuk dilatih
2. **Test Set** digunakan untuk mengevaluasi model yang sudah dilatih
3. **Validation Set** digunakan untuk mengevaluasi hasil dari training set. Setelah dirasa model yang dibuat dapat prediksi yang baik, lalu menggunakan test set untuk melakukan pemeriksaan ulang pada model.

Berikut diagram alir untuk melakukan penyesuaian terhadap model ML yang telah dibuat :

![ML-Flowchart](Image/ML-Flowchart.png)

#### Masalah dengan Dataset

Data yang terduplikat dapat mempengaruhi evaluasi pada model. Setelah dataset dipisah menjadi training set, validation set, dan test set, hapus semua contoh data di validation atau test set yang merupakan duplikat data di training set.

Test set atau validation set yang baik harus memenuhi kriteria sebagai berikut :

- Cukup besar untuk menghasilkan hasil pengujian yang signifikan secara statistik.

- Mewakili keseluruhan dataset. Dengan kata lain, jangan memilih test set yang memiliki karakteristik berbeda dari training set.

- Tidak mengandung data yang duplikat dari training set.

### Transformasi Data

Dalam machine learning, model hanya dapat dilatih menggunakan data dalam bentuk angka desimal (floating-point). Karena banyak fitur dalam dataset bukan angka (misalnya teks seperti nama jalan), maka perlu dilakukan transformasi ke bentuk numerik. Bahkan data numerik pun biasanya perlu dinormalisasi agar berada dalam rentang tertentu untuk mempercepat dan menstabilkan proses pelatihan. Transformasi ini merupakan langkah penting dalam pra-pemrosesan data sebelum digunakan oleh model.

Jika dataset terlalu besar, pilih subset data yang paling relevan dengan tujuan prediksi model untuk proses pelatihan. Selain itu, pastikan data yang digunakan tidak mengandung Personally Identifiable Information (PII) demi menjaga privasi, meskipun hal ini dapat memengaruhi performa model.

> ### Generalization
Generalization adalah kemampuan sebuah model machine learning untuk Bekerja dengan baik pada data baru yang belum pernah dilihat sebelumnya, bukan hanya pada data training. 
Tujuan utama machine learning bukan hanya menghafal data training, tetapi belajar pola yang berlaku umum sehingga bisa diterapkan pada data nyata atau baru, maka dari itu Generalization sangat penting.

Langkah generalization
- Kumpulkan data representatif
- Preprocessing: Bersihkan data, normalisasi, dan sebagainya
- Bagi data menjadi training/validasi/test
- Latih model
- Terapkan teknik anti overfitting yaitu: 

| Teknik                  | Penjelasan                                                        |
| ----------------------- | ----------------------------------------------------------------- |
|  **Regularization**    | Tambahan penalti pada loss untuk menghindari bobot besar (L1/L2)  |
|  **Dropout**           | Dalam neural net, menonaktifkan neuron acak saat training         |
|  **Early Stopping**    | Menghentikan training saat performa di validation mulai memburuk  |
|  **Data Augmentation** | Buat variasi baru dari data agar model belajar lebih fleksibel    |
|  **Cross-Validation**  | Membagi data ke banyak subset agar model diuji dari berbagai sisi |

- Evaluasi di data baru(*test set*) menggunakan metrik seperti accuracy, loss, precision, recall, AUC, dll. Kemudian Bandingkan performa antara training dan validation. Jika raining bagus tapi validation jelek (*overfitting*), Jika keduanya jelek(*underfitting*), dan jika seimbang (*generalize* dengan baik).
- Tuning dan retrain dengan menyesuaikan model atau hyperparameter berdasarkan hasil evaluasi, kemudian Ulangi proses hingga hasil di test set stabil dan optimal.
- validasi di dunia nyata.

> ### Overfitting

Overfitting terjadi saat model machine learning terlalu cocok dengan data pelatihan (training data), bahkan sampai menangkap noise atau data tidak relevan, sehingga Model bekerja sangat baik di training data, tapi buruk pada data baru (test/*real-world data*).

Ciri-ciri Overfitting:
1. Loss di training set terus menurun menjadi bagus, dan menyebabkan model sangat akurat di training set.
2. Loss di validation/test set memburuk setelah titik tertentu.
3. Gap besar antara akurasi training dan akurasi validation yang menunjukan "Divergensi".

Penyebab Overfitting:
1. Model terlalu kompleks karena terlalu banyak parameter untuk jumlah data yang tersedia.
2. Data terlalu sedikit jadi tidak cukup untuk membedakan variasi antara pola nyata dan noise.
3. Training terlalu lama jadi model belajar sangat lama sampai menangkap detail tidak penting seperti noise.

Cara Menegah overfitting:

| Teknik                   | Penjelasan                                                              |
| ------------------------ | ----------------------------------------------------------------------- |
|  **Regularization**     | Menambahkan penalti pada loss agar model tidak belajar terlalu kompleks. |
|  **Early Stopping**     | Hentikan training saat validation loss mulai naik.                      |
|  **Dropout**            | Nonaktifkan sebagian neuron saat training untuk mencegah ketergantungan. |
|  **More training data** | Tambahkan variasi data agar model belajar dari pola yang benar.          |
|  **Simpler model**      | Gunakan model dengan kompleksitas yang lebih rendah.                     |
|  **Cross-validation**   | Validasi model di banyak subset data agar hasil lebih stabil.            |

#### **Fitting, overfitting, and underfitting**
![fit_over_under](Image/over_under.png)

| Kondisi        | Ciri                                                         |
| -------------- | ------------------------------------------------------------ |
| Underfitting   | Model terlalu sederhana, performa buruk di semua data.       |
| Overfitting    | Model terlalu kompleks, hanya bagus di training.             |
| Generalization | Model cukup kompleks, performa baik di training dan test set.|

> ### Model complexity

Kompleksitas model merujuk pada seberapa fleksibel dan rumit suatu model dalam menangkap pola dari data. 
- Jika model sederhana, model hanya memiliki sedikit parameter dan hanya bisa belajar pola dasar.
- Jika model kompleks, model memiliki banyak parameter dan dapat menangkap pola rumit termasuk noise.

> ### Regularization

Regularization adalah teknik untuk mengurangi overfitting dengan menambahkan penalti terhadap parameter model yang besar ke dalam fungsi loss.Tujuannya mencegah model terlalu kompleks dan hanya fokus pada pola penting dari data.

Rumus:
$$ L_2\ regulation = w_1^2 + w_2^2 + ... + w_n^2 $$

contoh:
| **Weight** | **Value** | **Squared Value** |
| ---------- | --------- | ----------------- |
| w₁         | 0.2       | 0.04              |
| w₂         | -0.5      | 0.25              |
| w₃         | 5.0       | 25.00             |
| w₄         | -1.2      | 1.44              |
| w₅         | 0.3       | 0.09              |
| w₆         | -0.1      | 0.01              |
|            |           | **26.83** = total |
bobot (*weight*) yang nilainya mendekati nol tidak terlalu memengaruhi regularisasi L2, tetapi bobot yang besar dapat memberikan dampak yang sangat besar. Sebagai contoh, dalam perhitungan sebelumnya:

- Satu bobot saja (w₃) menyumbang sekitar 93% dari total kompleksitas.

- Lima bobot lainnya secara kolektif hanya menyumbang sekitar 7% dari total kompleksitas.

Regularisasi L2 mendorong nilai bobot mendekati nol, namun tidak pernah benar-benar membuat bobot menjadi nol sepenuhnya.

#### **Regulation Rate**
training attempts to minimize some combination of loss and complexity:
$$minimize(loss+complexity)$$

Pengembang model menyesuaikan seberapa besar pengaruh kompleksitas terhadap proses pelatihan model dengan mengalikan nilai kompleksitas tersebut dengan sebuah skalar yang disebut laju regularisasi (regularization rate). Karakter Yunani lambda (λ) biasanya digunakan untuk melambangkan laju regularisasi ini:
$$minimize(loss + λ\ complexity )$$
Artinya, pengembang model bertujuan untuk melakukan hal-hal berikut:
1. Laju regulasi tinggi
- Memperkuat pengaruh regularisasi, sehingga mengurangi kemungkinan overfitting.
- Cenderung menghasilkan histogram bobot model dengan ciri-ciri distribusi normal, dan rata rata bobot mendekati 0.
2. Laju regularisasi rendah
- Mengurangi pengaruh regularisasi, sehingga meningkatkan risiko overfitting.
- Cenderung menghasilkan histogram bobot model dengan distribusi yang datar (flat).

#### **Mennetukan laju regulasi (*regulation rate*)**
Laju regularisasi yang ideal adalah nilai yang menghasilkan model yang dapat mengeneralisasi dengan baik ke data baru yang belum pernah dilihat sebelumnya.
Namun sayangnya, nilai ideal ini sangat bergantung pada data, sehingga Anda perlu melakukan penyesuaian (*tuning*) terlebih dahulu.

#### ***Early Stopping***
Early stopping adalah metode regularisasi yang tidak bergantung pada perhitungan kompleksitas.
Sebaliknya, metode ini hanya berarti menghentikan proses pelatihan sebelum model benar-benar konvergen.
#### **Keseimbangan antara Learning Rate dan Regularization Rate**
Learning rate dan regularization rate cenderung menarik bobot (weight) ke arah yang berlawanan
| Parameter                 | Efeknya                                                       |
| ------------------------- | ------------------------------------------------------------- |
| **Learning rate tinggi**  | Menarik bobot **menjauhi nol** → bisa menyebabkan overfitting |
| **Regularization tinggi** | Menarik bobot **menuju nol** → bisa membuat prediksi buruk    |

> ### Interpretasi Loss Kurva
Kurva Loss sering kali sulit untuk diinterpretasikan. dibawah adalah contoh untuk menginterpretasi Loss Kurva

**1. Oscilating Loss Curve**

![loss_Osilasi](Image/oscilating%20loss.png)

Tiga hal yang bisa dilakukan untuk memperbaiki loss curve seperti ini
- Menurunkan learning rate
- Membersihkan data yang tidak valid atau salah label
- Kurangi set pelatihan menjadi sejumlah kecil contoh yang dapat dipercaya.

**2. Loss curve with a sharp jump**

![Loss_jump](Image/Loss-Curve-with-jump.png)

penyebab loss yang tiba-tiba melonjak tajam
- Jika data input mengandung NaN (Not a Number) menyebabkan ledakan loss (exploding loss) karena model tak dapat belajar dari data yang tidak valid.
- Outliers ekstrem dalam data menyebabkan pembaruan bobot yang ekstrem dan loss meningkat drastis dalam satu atau beberapa langkah.

**3. Test loss diverges from training loss**

![Loss_diverges](Image/Shrap-rise-validation-loss.png)

Jika kurva loss pada training set terus menurun, namun kurva loss pada test set (atau validation set) berhenti menurun dan justru meningkat, maka ini adalah tanda klasik dari overfitting.Artinya, model terlalu fokus pada data training bahkan sampai menghafalnya, tetapi gagal menggeneralisasi ke data baru (test/validasi).

**4. Loss curve gets stuck**

![Loss_stuck](Image/Loss-curve-stagnan.png)

Jika kurva loss terlihat tidak stabil, loncat-loncat, atau tidak menurun dengan mulus, kemungkinan besar Data training tidak diacak (shuffled) dengan baik. Akibatnya Model menerima pola data yang tidak acak atau berkelompok secara berturut-turut, menyebabkan gradien training berubah-ubah drastis dan hasil akhirnya adalah kurva loss yang erratik atau macet dan tidak konvergen secara efisien.

<br>

## **3. Model Machine Learning Lanjutan**
## Neural Network

**Neural Network** atau jaringan neural adalah model pembelajaran mesin yang dirancang untuk menemukan pola non-linear dalam data. Model ini menghindari eksperimen manual dengan fitur silang dan secara otomatis mempelajari representasi data yang optimal selama pelatihan. Komponen utama dari jaringan neural meliputi node (neuron), lapisan tersembunyi, dan fungsi aktivasi. Selama pelatihan, jaringan neural dioptimalkan menggunakan algoritma backpropagation untuk meminimalkan fungsi kerugian dan meningkatkan akurasi prediksi.

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
- [Dokumentasi Pandas (Untuk bagian Data)](https://pandas.pydata.org/docs/)

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*