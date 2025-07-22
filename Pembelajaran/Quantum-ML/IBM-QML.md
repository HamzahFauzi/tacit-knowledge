
---
---
---

<div align="center">
    <h1 style="font-size: 45px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #e63946; background: linear-gradient(45deg, #e63946, #1d3557); -webkit-background-clip: text; color: transparent; padding: 20px 40px; border: 4px solid transparent; border-radius: 12px; background-image: linear-gradient(45deg, #e63946, #1d3557);">
        IBM - Quantum Machine Learning
    </h1>
</div>

---
---
---

<br>
<br>

# Introduction

## 1. Komputasi Kuantum vs. Klasik & Definisi QML

* **Siklus Kompetisi** <br> Komputasi kuantum dan klasik saling mendorong batas kemampuan. Masalah yang pertama dipecahkan kuantum seringkali kemudian ditemukan solusinya di klasik, dan sebaliknya.
* **Keunggulan Spesifik Kuantum** <br> Ada masalah tertentu di mana komputasi kuantum dapat memiliki keunggulan yang terbukti, dengan syarat kemajuan dalam pengurangan kesalahan dan ketersediaan *qubit*.
* **QML sebagai Pelengkap** <br> Pembelajaran Mesin Kuantum (QML) adalah bidang menarik di mana komputasi kuantum dapat memperkaya atau melengkapi alur kerja ML klasik.
* **Fokus QML** <br> Sebagian besar fokus QML saat ini adalah pada penerapan **algoritma kuantum pada data klasik**. Ini karena data klasik sudah banyak dipelajari dan tersedia, serta adanya keterbatasan QRAM (memori kuantum) yang membuat pemrosesan data kuantum asli masih jauh dari aplikasi industri.
* **Jenis ML** <br> Pembahasan juga mencakup **Supervised Learning** (dengan data berlabel) dan **Unsupervised Learning** (data tanpa label).

## 2. Konsep Pemetaan Data & Kekuatan Kuantum

* **Pemetaan Dimensi Tinggi** <br> Banyak metode ML klasik dan kuantum melibatkan pemetaan data dari dimensi rendah ke **ruang dimensi yang lebih tinggi** agar data lebih mudah dipisahkan (misalnya, untuk klasifikasi).
* **Peran QML dalam Pemetaan** <br> Tujuan QML adalah menemukan "peta fitur kuantum" yang bisa memisahkan titik data secara efektif di ruang berdimensi tinggi, yang mungkin tidak efisien dilakukan secara klasik.

## 3. Mengelola Ekspektasi dan Batasan QML

* **Pentingnya "*Feature Engineering*"** <br> Banyak dataset dalam riset QML "direkayasa" khusus untuk menunjukkan kasus penggunaan sempit di mana kuantum berguna. Ini bukan "kecurangan", melainkan upaya eksplorasi.
* **Bukan Solusi Universal** <br> Tidak semua peta fitur kuantum lebih efisien dari yang klasik. Kekuatan kuantum datang dari cara novel sirkuit kuantum berinteraksi dengan struktur data kompleks.
* **Penjelasan Sederhana yang Kurang Memadai:**
    * Argumen "superposisi $2^N$ keadaan sekaligus" itu benar, tetapi tidak lengkap. Meskipun *qubit* bisa dalam superposisi, pengukuran hanya menghasilkan satu keadaan, sehingga tidak semua informasi dapat diekstrak secara instan.
    * Penggunaan **koefisien kompleks** dalam keadaan kuantum (vs. koefisien real positif di klasik) memungkinkan fenomena seperti interferensi, yang merupakan sumber kekuatan kuantum, namun bukan berarti "lebih banyak informasi" bisa langsung dibaca. Pernyataan ini harus hati-hati karena setelah pengukuran, probabilitas tetap real dan positif.
* **Dimensi Tinggi Bukan Jaminan Kekuatan** <br> ML klasik sudah dapat bekerja dengan dimensi tinggi tak terbatas (misalnya, melalui **Kernel Gaussian** yang dikombinasikan dengan **Kernel Trick** tanpa perlu memetakan data secara eksplisit). Jadi, kemampuan QML untuk mencapai dimensi tinggi saja tidak cukup untuk menunjukkan keunggulan.
* **"Paralelisme Eksponensial" Tidak Cukup** <br> Meskipun secara teoretis $N$ *qubit* bisa memproses $2^N$ keadaan paralel, keterbatasan pengukuran membuat kita tidak bisa langsung membaca semua hasil. Kekuatan terletak pada desain algoritma yang cerdas untuk meningkatkan probabilitas hasil yang benar.

## 4. Dekuantisasi: Batasan Keunggulan Kuantum

* **Definisi Dekuantisasi** <br> Proses di mana algoritma klasik ditemukan untuk meniru kinerja algoritma kuantum (biasanya dengan kompleksitas waktu yang hanya **polinomial** lebih lambat). Ini membantu mengidentifikasi batas sebenarnya dari keunggulan kuantum.
* **Contoh Ewin Tang** <br> Penelitian Tang menunjukkan bahwa algoritma klasik bisa seefisien algoritma kuantum dalam sistem rekomendasi, menantang asumsi keunggulan eksponensial kuantum untuk masalah tersebut.
* **Overhead Pemuatan Data** <br> Banyak algoritma QML mengasumsikan data sudah dalam format kuantum. Namun, waktu untuk **mengkodekan data klasik ke kuantum** bisa sangat lambat. Jika waktu *encoding* ini dihitung, algoritma kuantum mungkin tidak lagi mengungguli rekan klasiknya.
* **Efisiensi Keseluruhan** <br> Meskipun sebuah algoritma tidak dapat didekuantisasi (misalnya, menggunakan **Algoritma Shor** yang unik kuantum), bukan berarti algoritma tersebut efisien secara keseluruhan jika bagian non-kuantumnya sangat tidak efisien untuk tujuan yang dimaksudkan.

## 5. Bukti Keberadaan (*Existence Proof*) Keunggulan Kuantum Nyata

* **Studi IBM Quantum (2021)** <br> Para peneliti menunjukkan percepatan eksponensial yang "*end-to-end*" (termasuk waktu *encoding*) dan "*robust*" (tangguh terhadap kesalahan) untuk masalah klasifikasi yang berbasis **logaritma diskrit**. Masalah ini secara teoretis sulit bagi klasik tetapi cocok untuk kuantum.
* **Pentingnya Masalah yang Tepat** <br> Keunggulan kuantum terjadi pada masalah yang **sulit secara klasik dan cocok untuk algoritma kuantum**. Tidak realistis mengharapkan percepatan untuk masalah yang sudah baik diatasi oleh klasik.
* **Tugas Explorasi** <br> Mengidentifikasi kasus ideal untuk QML adalah tanggung jawab besar bagi peneliti, termasuk para pelajar kursus ini.

<br>
<br>

# Classical ML Review

Pada bagian ini membahas pemahaman dasar-dasar Pembelajaran Mesin (ML) Klasik, khususnya *Support Vector Machine* (SVM) dan Jaringan Saraf (Neural Networks/NN), sebagai fondasi sebelum mendalami Pembelajaran Mesin Kuantum (QML).

---

### I. Kategori Utama Pembelajaran Mesin Klasik

ML adalah kumpulan algoritma untuk menganalisis dan menarik inferensi dari pola data tanpa pemrograman eksplisit. Ada tiga kategori utama, sebagai berikut :

1.  **Pembelajaran Terawasi (Supervised Learning)**
    * **Definisi**<br>Menggunakan data yang **sudah diberi label** (input dan output yang benar diketahui).
    * **Tujuan**<br>Mempelajari hubungan antara input dan label untuk digeneralisasi ke data baru.
    * **Contoh Tugas**
        * **Klasifikasi:** Memprediksi kategori (misal: spam/bukan spam).
        * **Regresi:** Memprediksi nilai numerik kontinu (misal: harga rumah).

2.  **Pembelajaran Tanpa Terawasi (Unsupervised Learning)**
    * **Definisi**<br>Menggunakan data yang **tidak diberi label**.
    * **Tujuan**<br>Menemukan pola, struktur, atau hubungan tersembunyi dalam data.
    * **Contoh Tugas**
        * **Clustering (Pengelompokan) :** Mengelompokkan data serupa.
        * **Dimensionality Reduction (Reduksi Dimensi) :** Mengurangi fitur data.
        * **Model Generatif :** Membuat data baru yang mirip.

3.  **Pembelajaran Penguatan (Reinforcement Learning)**
    * **Definisi**<br>"Agen" berinteraksi dengan "lingkungan", mengambil tindakan dan menerima "hadiah" atau "hukuman" sebagai umpan balik.
    * **Tujuan**<br>Belajar serangkaian tindakan terbaik untuk memaksimalkan hadiah.
    * **Contoh Tugas**<br>Mengajari robot berjalan, AI bermain game.

---

### II. Pengenalan Kuantum ke Pembelajaran Mesin

Keterlibatan kuantum dalam ML dikategorikan berdasarkan jenis data dan perangkat pemroses berikut :

* **CC (Classical Data - Classical Computer)**<br>ML klasik murni (data klasik diolah komputer klasik). Ini adalah pengaturan paling umum saat ini.
* **QC (Quantum Data - Classical Computer)**<br>Data kuantum (misal: hasil pengukuran kuantum) diolah oleh komputer klasik.
* **CQ (Classical Data - Quantum Computer)**<br>**Fokus utama QML saat ini.** Data klasik diolah oleh komputer kuantum.
* **QQ (Quantum Data - Quantum Computer)**<br>Data kuantum diolah oleh komputer kuantum (potensi masa depan, misal dengan QRAM).

---

### III. Support Vector Machine (SVM) Klasik

SVM adalah algoritma klasifikasi yang bertujuan mencari **bidang pemisah (*hyperplane*)** optimal antara dua kelas data.

* **Ide Utama**<br>Menemukan *hyperplane* yang memaksimalkan **margin** (jarak) ke titik data terdekat di setiap kelas (disebut ***support vectors***).
* **Formulasi**
    * **Primal ($f_1(\vec{x}) = \Theta^T \Phi(\vec{x}) + b$)**<br>Masalah optimasi asli yang mencari parameter $\Theta$ (vektor yang menentukan *hyperplane*) dan bias $b$.
        * **Parameter ($\Theta$)**<br>Nilai internal model yang disesuaikan selama pelatihan untuk menemukan hubungan fitur-label (bukan input/output).
        * **Masalah Dimensi Tinggi**<br>Menghitung *inner product* ($\Theta^T \Phi(\vec{x})$) di ruang dimensi tinggi bisa **sangat mahal atau tidak mungkin** jika $\Phi(\vec{x})$ memetakan ke dimensi yang sangat tinggi (misal, tak terbatas).
    * **Dual ($f_2(\vec{x}) = \sum_{i=1}^n \alpha_i y_i \Phi^T(\vec{x}_i) \Phi(\vec{x}) + b$)**<br>Formulasi ulang masalah primal yang mengubah variabel optimasi menjadi $\alpha_i$.
        * **Keuntungan Dual**<br>*Inner product* hanya terjadi antara **vektor fitur yang dipetakan** ($\Phi^T(\vec{x}_i) \Phi(\vec{x})$) dari dua titik data. Ini kunci untuk *Kernel Trick*.

* **Pemetaan ke Dimensi Lebih Tinggi ($\Phi$)**
    * Terkadang data tidak bisa dipisahkan secara linier di dimensi aslinya. $\Phi$ memetakan data ke ruang dimensi lebih tinggi (misal, menambahkan fitur baru $x_1 x_2$) agar menjadi terpisah secara linier.
    * **Informasi Penting**<br>Kemampuan memetakan ke dimensi tinggi bukanlah kekuatan unik kuantum, karena ML klasik juga bisa (misalnya, Kernel Gaussian ke dimensi tak terbatas).

* **Fungsi Kernel dan Kernel Trick**
    * **Produk Dalam (*Inner Product*)**<br>Operasi yang mengambil dua vektor dan menghasilkan satu angka tunggal, mengukur "kemiripan" atau "tumpang tindih" di antara mereka (contoh: $\vec{A} \cdot \vec{B} = a_1 b_1 + a_2 b_2 + \dots + a_n b_n$). Simbol 'T' ($\Theta^T \Phi$) menunjukkan transpose yang digunakan dalam notasi *inner product*.
    * **Fungsi Kernel ($k(\vec{x}_i, \vec{x}_j)$)**<br>Sebuah fungsi yang secara langsung menghitung hasil *inner product* dari dua vektor fitur yang telah dipetakan ($\Phi^T(\vec{x}_i) \Phi(\vec{x}_j)$), **tanpa perlu secara eksplisit menghitung atau mengetahui vektor $\Phi(\vec{x})$ itu sendiri**.
    * **Kernel Trick**<br>Teknik yang memungkinkan kita bekerja di ruang berdimensi sangat tinggi (bahkan tak terbatas) tanpa biaya komputasi yang tinggi, karena kita hanya perlu menghitung fungsi kernel di ruang dimensi rendah.
    * **Matriks Kernel**<br>Hasil perhitungan fungsi kernel untuk semua pasangan data membentuk matriks simetris positif semi-definit yang digunakan dalam optimasi SVM.

* **Kernel Kuantum:**
    * Menginterpretasikan pengkodean data $\vec{x}$ ke keadaan kuantum $|\Phi(\vec{x})⟩$ sebagai sebuah peta fitur.
    * **Estimasi Produk Dalam Kuantum**<br>Produk dalam antara dua keadaan kuantum $\langle\psi|\phi\rangle$ terkait dengan probabilitas mengukur keadaan $|\phi\rangle$ dari keadaan $|\psi\rangle$. Dalam QML, sirkuit kuantum seperti $\Phi^\dagger(\vec{x}_i) \Phi(\vec{x}_j)$ digunakan untuk mengestimasi produk dalam antara dua titik data yang dipetakan secara kuantum, seperti pada gambar di bawah ini :

    ![QML Circuit](image_QuantumML/QML-circuit.png)
    
    * Dengan menjalankan sirkuit ini berulang kali dan melakukan pengukuran, kita dapat mengestimasi probabilitas ($P_{|0⟩} = |\langle\Phi(\vec{x}_i)|\Phi(\vec{x}_j)\rangle|^2$) yang berhubungan langsung dengan nilai kernel (kemiripan) antar data. Matriks kernel yang dihasilkan kemudian digunakan oleh SVM klasik.

---

### IV. Perbandingan Kernel Klasik vs. Kuantum dalam SVM

Inti dari metode Kernel, baik klasik maupun kuantum adalah untuk **menemukan kemiripan (inner product)** antar titik data. Perbedaannya terletak pada **bagaimana *inner product* tersebut dihitung atau diestimasi**. Setelah *inner product* diperoleh, hasilnya akan membentuk matriks kernel yang kemudian digunakan sebagai input untuk algoritma **SVM klasik** dalam menemukan *hyperplane* pemisah.

#### **1. Kernel Klasik (Menggunakan Kernel Trick)**
* **Tujuan**<br>Mendapatkan nilai *inner product* ($⟨Φ(x_i)∣Φ(x_j)⟩$) antara dua vektor fitur.
* **Mekanisme**<br>Menggunakan **fungsi kernel matematika** ($k(x_i, x_j)$). Fungsi ini dirancang untuk secara langsung menghitung *inner product* di ruang dimensi tinggi, tanpa perlu secara eksplisit memetakan data atau mengetahui bentuk pemetaan $\Phi$. Ini dikenal sebagai **"Kernel Trick"**, yang memungkinkan efisiensi komputasi.
* **Output**<br>Nilai numerik tunggal (kemiripan).
* **Lanjutan**<br>Nilai *inner product* dari semua pasangan data mengisi **matriks kernel klasik** sebagai input untuk SVM klasik.

#### **2. Kernel Kuantum (Menggunakan Quantum Kernel Estimation)**
* **Tujuan**<br>Mendapatkan nilai *inner product* ($∣⟨Φ(x_i)∣Φ(x_j)⟩∣^2$) antara dua vektor fitur yang dienkode dalam keadaan kuantum.
* **Mekanisme**<br>Menggunakan **proses komputasi kuantum** yang melibatkan sirkuit dan pengukuran, bukan fungsi matematika klasik.
    * **Inisialisasi**<br>Semua *qubit* dimulai dalam keadaan dasar $∣0...0⟩$.
    * **Pemetaan Fitur Kuantum**<br>Salah satu titik data ($x_j$) dienkode ke dalam keadaan kuantum ($∣Φ(x_j)⟩$) melalui gerbang kuantum.
    * **Inversi Pemetaan Fitur Lain**<br>Keadaan kuantum yang merepresentasikan titik data lain ($x_i$) "dibalik" atau "dikonjugasikan" ($Φ^†(x_i)$) dan diterapkan. Ini membentuk keadaan di mana probabilitas pengukuran $∣0...0⟩$ akan mencerminkan *inner product* antara $∣Φ(x_i)⟩$ dan $∣Φ(x_j)⟩$.
    * **Pengukuran Probabilistik**<br>Sirkuit dijalankan berulang kali untuk mengukur probabilitas mendapatkan kembali keadaan awal $∣0...0⟩$.
    * **Estimasi**<br>Probabilitas yang diestimasi ini ($P_{∣0...0⟩} = ∣⟨Φ(x_i)∣Φ(x_j)⟩∣^2$) secara langsung terkait dengan kuadrat *inner product* kuantum, dari mana nilai kemiripan dapat disimpulkan.
* **Output**<br>Estimasi nilai numerik tunggal (kemiripan).
* **Lanjutan**<br>Nilai *inner product* yang diestimasi secara kuantum dari semua pasangan data mengisi **matriks kernel kuantum** sebagai input untuk SVM klasik.

Singkatnya, **Kernel Klasik** mengandalkan **fungsi matematika** yang efisien, sedangkan **Kernel Kuantum** memanfaatkan **sifat-sifat fundamental mekanika kuantum** (seperti superposisi, interferensi, dan pengukuran probabilistik) untuk mencapai tujuan yang sama dalam menghitung kemiripan antar data.

---

### V. Jaringan Saraf (Neural Networks) Klasik

NN adalah model komputasi yang terinspirasi otak, terdiri dari neuron (*node*) yang tersusun dalam lapisan dan terhubung melalui bobot.

* **Struktur**<br>Lapisan input, lapisan tersembunyi (jika ada), dan lapisan output.
* **Perceptron**<br>Unit dasar NN. Menerima input, menghitung produk dalam dengan bobot, menambah bias, dan menerapkan **fungsi aktivasi non-linier ($\sigma$)**.
* **Pentingnya Non-Linieritas**<br>Fungsi aktivasi non-linier adalah **kritis** agar NN dapat mempelajari pola kompleks. Tanpa non-linieritas, NN hanya akan menjadi model linier.
* **Pelatihan**<br>Dimulai dengan bobot dan bias acak, kemudian disesuaikan (dioptimalkan) menggunakan ***cost function*** (misalnya, Mean Squared Error/MSE) dan algoritma seperti **gradient descent** untuk meminimalkan *cost*.

---

### VI. Variational Quantum Classifiers (VQC) dan Jaringan Saraf Kuantum (QNN)

VQC adalah algoritma QML jangka menengah yang seringkali (namun tidak selalu) mengadopsi struktur mirip NN klasik, disebut QNN.

* **Perceptron Kuantum**<br>Membutuhkan cara untuk mengimplementasikan non-linieritas karena sirkuit kuantum dasar bersifat linier (*unitary*).
    * **Sumber Non-Linieritas di Kuantum**<br>Umumnya melalui **pengukuran** (yang meruntuhkan superposisi), atau teknik lain seperti transformasi Fourier kuantum, pengukuran di tengah sirkuit, dan *tracing out* *qubit*.
* **QNN**
    * **Proses**<br>Mengkodekan data input ($U$), menerapkan sirkuit bobot kuantum ($W$) yang berisi parameter yang dapat dilatih, dan mengakhiri dengan pengukuran.
    * **Komponen**<br>Memiliki bagian linier (pengkodean, bobot) dan non-linier (pengukuran), mirip dengan NN klasik.
    * **Optimasi**<br>Masih memerlukan minimisasi klasik untuk menyesuaikan parameter variasi pada sirkuit bobot.

* **Generalisasi : Data Reuploading**
    * **Konsep**<br>Teknik di mana blok pengkodean data ($U$) **diulang** di antara blok sirkuit bobot variasi ($W$).
    * **Tujuan**<br>Meningkatkan ekspresivitas dan kekuatan representasi model, memungkinkan QNN mengaproksimasi fungsi kompleks, bahkan dengan jumlah *qubit* yang sedikit.
    * **Perbedaan dengan NN Klasik:**
        * **QNN**<br>`Data reuploading` penting karena operasi kuantum dasar bersifat linier, sehingga teknik ini (bersama pengukuran) secara efektif memperkenalkan non-linieritas dan kemampuan memproses ulang informasi yang kompleks.
        * **NN Klasik**<br>Tidak mengadopsi `data reuploading` dengan cara yang sama karena sudah memiliki fungsi aktivasi non-linier di setiap neuronnya. Konsep serupa mungkin ada (misal: *residual connections* di ResNet, *memory states* di RNN, *concatenation of features*), tetapi tujuannya dan implementasinya berbeda. NN klasik fokus pada pembangunan representasi hierarkis abstrak.

<br>
<br>

# Data Encoding

