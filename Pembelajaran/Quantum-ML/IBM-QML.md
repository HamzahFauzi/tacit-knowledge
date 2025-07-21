
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