# Tutorial: Materi Pembelajaran Material Machine Learning

## Daftar Isi
  [***Introdcution***](#introduction)
1. Sejarah Data dan Data Science
2. Data Science Menuju Material Data Science
3. Dasar Matematika dalam Data Science
4. Material Science Datasets dan Data Generation

## *Introduction*

## **1.  Sejarah Data dan Data Science**
### 1.1 Darimana Angka Datang ?

Pada awal tahun 3400 sebelum masehi, Bangsa Sumeria telah memperkenalkan sistem angka yang ditulis pada lempengan tanah liat. Sekitar tahun 2000 sebelum masehi bangsa Babilonia membuat sistem angka desimal dan telah melakukan perhitungan pendekatan nilai phi (π ≈ 3.125). Pada tahun 300 sebelum masehi bangsa Babilonia juga menciptakan alat bernama *abacus* sebaga alat perhitungan. Walaupun angka romawi sudah ada pada tahun 1000 sebelum masehi, Eropa harus menunggu 2 abad lagi sebelum sistem angka Indo-Arab (yang digunakan saat ini).  Masih banyak penemuan angka lainnya seperti angka "0" dan sistem angka biner pertama. Sekarang kita akan membahas penggunaan angka selain jual beli seperti penggunaan angka dalam bidang astronomi dan memprediksi lintasan benda-benda di langit.

### 1.2 The Ancient Roots of Data Science

Bangsa Babilonia kuno telah melakukan segalanya yang berhubungan dengan ilmu data (Data Science). Data science tidak akan ada tanpa adanya perkembangan sejarah yang ada. Pada sesi ini akan dijelaskan bagaimana penemuan-penemuan angka yang ada

![Roadmap Numbers](./Image/Roadmap%20Numbers.png)

#### 1.2.1 Bangsa Babilonia Kuno (1800-600 SM)

Ketika bangsa Babilonia mengamati langit malam, mereka mengenali ada dua jenis benda langit. Yang pertama adalah bintang yang bergerak dengan pola melingkar dan dapat berkelap kelip. Yang kedua adalah benda langit yang bergerak tidak beraturan dan dikenal sebagai gerak *retograd*. Bangsa Babilonia pada masanya hanya mengenali merkurius, venus, mars jupiter, saturnus, bulan dan bintang. Namun bangsa Babilonia tidak dapat menjelaskan pergerakan dari planet ini, sehingga mereka mengasumsikan bahwa planet tersebut dikendalikan oleh Dewa. Model pergerakan yang dibuat bangsa memiliki tujuan untuk menentukan kalender kapan untuk bertani, panen bahkan untuk pergi perang.  

#### 1.2.2 Zaman Klasik Kuno (750-600 SM)

Setelah runtuhnya bangsa Babilonia pada 539 SM, Sebagian besar pengetahuan mereka hampir lenyap. Namun untungnya, beberapa ilmu pengetahuan tentang astronomi telah diteruskan ke orang Yunani. Anaximenes (±585–525 SM) membangun model kosmologi berdasarkan pemikiran Babilonia, tetapi tanpa melibatkan dewa-dewa. Ia memperkenalkan konsep setengah bola konsentris untuk menjelaskan pergerakan bintang dan planet, serta menciptakan unsur aether yaitu zat tak terlihat seperti kristal yang diyakini mendasari langit.

Sayangnya, Anaximenes tidak mampu menjelaskan gerak planet yang kompleks. Solusinya datang dari *Eudoxus of Cnidus* (±408–355 SM), murid Plato, yang  menambahkan banyak bola berputar. Bola tersbut di antaranya adalah 3 bola matahari dan bulan, serta 4 bola untuk masing-masing dari 5 planet. Kombinasi gerakan dari dua bola berbeda ini digunakan untuk menjelaskan gerak retrograd secara parsial. Secara keseluruhan, model ini memerlukan 27 bola langit. Aristoteles (384–322 SM) kemudian memperluas model ini menjadi 56 bola, karena hanya dengan cara itulah ia bisa menjelaskan variasi tingkat kecerahan bintang. Meskipun model ini terlihat canggih pada zamannya, dalam konteks pembelajaran mesin (machine learning) modern, pendekatan seperti ini dapat dianggap sebagai bentuk overfitting. Artinya, model terlalu disesuaikan dengan data pengamatan sehingga kehilangan kemampuan untuk menyederhanakan atau menangkap pola yang lebih umum. Dengan kata lain, kompleksitas model tidak lagi mencerminkan pemahaman mendalam terhadap fenomena, melainkan hanya upaya memaksa kecocokan terhadap data yang ada.

Sayangnya, bahkan model-model sebelumnya belum mampu menjelaskan semua fenomena langit yang diamati, termasuk perubahan fase Bulan seperti bulan sabit dan purnama. Baru beberapa abad kemudian, ilmuwan Romawi Claudius Ptolemy (sekitar 100–170 M) muncul dengan gagasan baru, meskipun sebagian sudah pernah disebut oleh ilmuwan Yunani sebelumnya. Dalam modelnya, Ptolemy membayangkan bahwa planet-planet menempel pada semacam "roda langit" yang terhubung dengan bola-bola langit. Ia juga menempatkan Bumi dalam posisi sedikit tidak simetris (eksentris) terhadap pusat, sehingga planet-planet tampak bergerak dengan kecepatan berbeda. Model geosentris ini sangat kompleks, terdiri dari sekitar 80 elemen geometris seperti lingkaran dan bola, namun memiliki tingkat akurasi yang tinggi. Model ini mampu memprediksi fenomena seperti gerhana, dan Ptolemy juga menyusun tabel astronomi serta alat bantu lain untuk menghitung posisi Bulan, Matahari, dan planet-planet. Meskipun mengandung banyak asumsi fisika yang keliru dan sangat rumit, model ini menjadi standar tertinggi dalam astronomi selama lebih dari seribu tahun.

#### 1.2.3 Zaman Medieval (500-1500)

Abad Pertengahan merupakan masa suram bagi masyarakat Eropa, termasuk bagi perkembangan ilmu pengetahuan. Kelaparan, perang, dan wabah penyakit menyebabkan penurunan drastis jumlah penduduk, termasuk para ilmuwan. Invasi dan migrasi besar-besaran menciptakan kondisi yang tidak kondusif bagi kemajuan ilmu. Di tengah keterpurukan itu, muncul Thomas Aquinas (1225–1274) sebagai salah satu pemikir cemerlang yang langka pada masanya. Ia mencoba menyelaraskan ilmu astronomi dengan ajaran teologi. Salah satu kontribusinya adalah merumuskan lima argumen untuk membuktikan keberadaan Tuhan. Hal ini mencerminkan semangat zaman tersebut yang masih sangat teologis. Namun, semua argumen tersebut kemudian dibantah oleh William of Occam, seorang filsuf yang dikenal dengan prinsip Occam’s Razor. Prinsip ini—yang akan dibahas lebih lanjut dan memiliki pengaruh penting dalam dunia ilmu data modern (data science), karena menekankan pentingnya kesederhanaan dalam membangun model atau penjelasan ilmiah.

#### 1.2.4 Zaman Renaisans (Sekitar 1500-1700)

