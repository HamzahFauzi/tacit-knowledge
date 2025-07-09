
---
---
---

<div align="center">
    <h1 style="font-size: 45px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #e63946; background: linear-gradient(45deg, #e63946, #1d3557); -webkit-background-clip: text; color: transparent; padding: 20px 40px; border: 4px solid transparent; border-radius: 12px; background-image: linear-gradient(45deg, #e63946, #1d3557);">
        Quantum Computing
    </h1>
</div>

---
---
---

<br>
<br>

# PART 1 : Qubit & Gerbang Kuantum
## Apa Itu Komputasi Kuantum?
Bayangkan komputer biasa seperti kalkulator super cepat yang bekerja dengan angka 0 dan 1. Nah, komputer kuantum adalah jenis komputer baru yang bekerja dengan cara yang sangat berbeda dan jauh lebih canggih. Ia tidak hanya menggunakan 0 dan 1, tapi juga campuran dari keduanya secara bersamaan! Di sinilah peran utama qubit, unit dasar informasi kuantum.

## Apa Itu Qubit?
Bayangkan sebuah koin. Kalau kamu melemparnya, hasilnya bisa kepala (0) atau ekor (1). Tapi qubit seperti koin yang sedang berputar di udara dia bisa berada dalam keadaan kepala dan ekor secara bersamaan. Fenomena ini disebut superposisi.

Dalam komputer biasa 1 bit = 0 atau 1,  Dalam komputer kuantum 1 qubit = kombinasi dari 0 dan 1 sekaligus. Artinya **qubit dapat menyimpan lebih banyak kemungkinan informasi dalam satu waktu**.  
Qubit juga tidak sekadar angka. Ia direpresentasikan sebagai vektor dua dimensi, yaitu arah di dalam ruang yang disebut *state space* (ruang keadaan). Dua arah paling dasar adalah:
- $|0⟩$ → vektor $[1, 0]$ , seperti  bit 0.
- $|1⟩$ → vektor $[0, 1]$ , seperti  bit 0.  
  
Namun qubit bisa berada di antara keduanya — misalnya dalam keadaan:
$0.6|0⟩ + 0.8|1⟩$, yang secara visual seperti panah yang condong ke arah tertentu antara dua ujung.

## Visualisasi Qubit
![QUBIT-VISUALITATION](/Pembelajaran/Quantum-ML/image_QuantumML/qubit_visualisation.png)

Untuk membantu membayangkan, bayangkan sebuah bola transparan. Setiap posisi pada permukaan bola ini bisa mewakili satu keadaan qubit. Arah panah di permukaan bola menunjukkan seperti apa “campuran” dari 0 dan 1 dalam qubit.  
Jika panah mengarah tepat ke atas, itu artinya keadaan 0 $(|0⟩)$. Jika mengarah ke bawah, itu keadaan 1 $(|1⟩)$. Dan arah lainnya menggambarkan campuran probabilitas antara keduanya.

## Superposisi : Lebih dari sekedar 0 dan 1

Superposisi adalah konsep yang membuat qubit unik. Ia bisa berada dalam "campuran" dari 0 dan 1, dan baru akan "memilih salah satu" saat kamu melihatnya (diukur). Jadi, selama belum diukur, dia menyimpan potensi jawaban ganda.  
Keadaan campuran seperti $0.6|0⟩ + 0.8|1⟩$ disebut superposisi.
## Amplitudo : Pengaruh masing masing arah
Angka-angka 0.6 dan 0.8 disebut **amplitudo**, yang menunjukkan seberapa besar “pengaruh” masing-masing arah ($|0⟩$ dan $|1⟩$) dalam keadaan akhir. 
- Pangkat dua dari amplitudo menyatakan peluang hasil pengukuran.
- Jadi, 0.6² = 36% kemungkinan hasilnya 0, dan 0.8² = 64% kemungkinan hasilnya 1. 

Jumlah total dari kuadrat amplitudo harus = 1. Ini disebut **normalisasi**. Artinya, peluang hasil harus selalu 100%.

## Apa arti fisik Qubit ?
Seperti bit disimpan sebagai arus listrik atau magnet kecil dalam chip komputer, qubit juga disimpan dalam sistem fisik tertentu bisa dalam elektron, foton (partikel cahaya), atau atom. Tapi apa mediumnya tidak begitu penting di tahap awal. Yang penting adalah bahwa qubit adalah representasi informasi dalam bentuk matematis dan kita bisa mengolahnya.

## *Catatan PART 1*

> ### Qubit sebagai Vektor
$$
∣ψ⟩=α∣0⟩+β∣1⟩,∣α∣² +∣β∣²=1
$$

Inilah inti “state space” qubit.

> ### Normalisasi dan Informasi Terbatas
Kita tidak bisa menyimpan panjang α atau β secara presisi—measurement hanya mengungkap 0 atau 1, dan setelahnya amplitudo hilang, jadi tidak bisa menyimpan informasi tak terbatas.

> ### Visualisasi dengan Bloch Sphere
Qubit dapat divisualisasikan sebagai titik di permukaan bola Bloch:
- Sudut θ menentukan probabilitas (dekat kutub Z → probabilitas besar ke 0 atau 1).
- Sudut φ menyangkut fase kompleks.
- Rotasi pada sphere sebanding dengan penerapan gerbang. Misalnya X memutar 180° di sumbu X.

![Bloch Sphere – Geometric Representation of Quantum State](/Pembelajaran/Quantum-ML/image_QuantumML/geometric-of-quantum-state.jpeg)

> ### Gerbang Dasar (Unitaritas)
- **X (NOT)**: menukar |0⟩↔|1⟩ (berfunctional sebagai kliniskan X = \[0 1; 1 0]).
- **H (Hadamard)**: mengonversi basis ke superposisi, contoh: H|0⟩ = (|0⟩+|1⟩)/√2.
- Semua gerbang adalah *unitary* → preserve panjang vektor → U†U = I.
- **Catatan manusiawi:** “Bayangkan memutar panah di Bloch Sphere—itulah yang dilakukan gerbang quantum.”

<br>
<br>

# PART 2 : Gerbang Logika Kuantum (*quantum logic gates*)

## Apa Itu Gerbang Logika Kuantum?
Gerbang logika kuantum adalah cara untuk memanipulasi informasi kuantum, yaitu keadaan dari qubit (unit terkecil dalam komputasi kuantum). Konsep ini mirip dengan gerbang logika dalam komputer klasik (seperti AND, OR, NOT), tetapi bekerja berdasarkan prinsip mekanika kuantum. Gerbang-gerbang ini menjadi fondasi semua perhitungan dalam komputer kuantum, memungkinkan operasi seperti teleportasi kuantum hingga algoritma kuantum yang kompleks.

## Gerbang NOT Kuantum : Gerbang X
Gerbang NOT dalam dunia kuantum disebut juga sebagai **gerbang X**. Ia bekerja dengan membalik Qubit.
- Jika input adalah $∣0⟩$ maka hasilnya $∣1⟩$
- Jika input adalah $∣1⟩$ maka hasilnya $∣0⟩$

Untuk superposisi seperti $α∣0⟩ + β∣1⟩$, gerbang X akan menukar posisi amplitudonya menjadi $α∣1⟩ + β∣0⟩$. Dalam representasi matriks, gerbang X ditulis sebagai:
$$
X = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$
Dalam diagram sirkuit kuantum, gerbang ini digambarkan sebagai kotak bertuliskan “X” yang terletak di atas garis waktu qubit.
## Kuantum Wire
Pernahkah kamu membayangkan ada kabel listrik yang saking kecilnya, elektron-elektron yang mengalir di dalamnya mulai berkelakuan aneh, mengikuti aturan fisika kuantum? Nah, itulah gambaran sederhana dari kuantum wire.  
Memahami Kuantum Wire: Kabel Super Kecil dengan Aturan Ajaib
Pernahkah kamu membayangkan ada kabel listrik yang saking kecilnya, elektron-elektron yang mengalir di dalamnya mulai berkelakuan aneh, mengikuti aturan fisika kuantum? Nah, itulah gambaran sederhana dari kuantum wire!

Apa Itu Kuantum Wire?
Secara sederhana, kuantum wire (atau sering juga disebut nanowire) adalah kawat atau struktur konduktor yang memiliki ukuran sangat, sangat kecil, biasanya hanya beberapa nanometer (satu nanometer itu sepermiliar meter!). Ukuran ini begitu kecil hingga sebanding dengan "panjang gelombang de Broglie" elektron, yaitu ukuran alami yang dimiliki elektron ketika bergerak.

Karena ukurannya yang super mini ini, gerakan elektron di dalam kawat tersebut menjadi sangat terbatas. Bayangkan seperti air yang mengalir di pipa yang sangat sempit. Air hanya bisa bergerak maju atau mundur, tidak bisa bergerak bebas ke samping. Demikian pula elektron di kuantum wire; mereka "terjebak" dalam dua dimensi (lebar dan tinggi kawat), sehingga hanya bisa bergerak bebas dalam satu dimensi (sepanjang kawat).
### Tantangan Kuantum Wire
Quantum wire atau “kabel kuantum” menggambarkan qubit yang dibiarkan mengalir tanpa dimanipulasi. Secara teori ini sederhana, tetapi secara fisik sangat sulit karena qubit sangat rapuh dan mudah terganggu oleh lingkungan. Menyimpan qubit dalam waktu lama (misalnya menggunakan foton atau atom) menjadi tantangan besar karena ketidakstabilannya.
### Contoh Penerapan Kuantum Wire
Meskipun masih dalam tahap penelitian dan pengembangan yang intens, kuantum wire memiliki potensi besar untuk merevolusi berbagai bidang teknologi:

- **Elektronik Ultra-Cepat**: Bisa digunakan untuk membuat transistor yang jauh lebih cepat dari yang ada saat ini, interkoneksi (jalur data) dalam chip yang lebih efisien, dan perangkat logika yang mengonsumsi daya sangat rendah. Bayangkan smartphone yang jauh lebih cepat dan baterai yang tahan lebih lama!

- **Lampu LED dan Laser Efisien**: Kuantum wire dapat meningkatkan efisiensi dan kualitas warna lampu LED serta membuat laser yang lebih baik untuk berbagai aplikasi.

- **Sel Surya dan Sel Bahan Bakar**: Dengan kemampuan untuk meningkatkan penyerapan cahaya dan pengumpulan muatan, kuantum wire bisa membuat sel surya (panel surya) menjadi jauh lebih efisien dalam mengubah cahaya matahari menjadi listrik.

- **Sensor Super Sensitif**: Karena rasio luas permukaan terhadap volumenya yang sangat tinggi, kuantum wire dapat digunakan untuk membuat sensor yang sangat peka, misalnya untuk mendeteksi bahan kimia tertentu atau bahkan tanda-tanda biologis.
## Sirkuit Dua Gerbang X: Identitas
Menempatkan dua gerbang X secara berurutan akan mengembalikan qubit ke kondisi semula. Ini serupa dengan membalikkan koin dua kali. Secara matematis:
$$
X(X(α∣0⟩ + β∣1⟩)) = α∣0⟩ + β∣1⟩
$$
Secara matriks, ini berarti perkalian dua matriks X menghasilkan matriks identitas (tidak mengubah apapun).

## Gerbang Hadamard (H) : Campuran Unik
Gerbang Hadamard (H) adalah gerbang kuantum pertama yang memperlihatkan perilaku unik dunia kuantum. Ia menciptakan superposisi dari keadaan dasar:
- $H∣0⟩ = \frac{(∣0⟩ + ∣1⟩)}{√2} $, artinya qubit berada ditengah tengah antara 0 dan 1.
- $H∣1⟩ = \frac{(∣0⟩ - ∣1⟩)}{√2} $

Jika diaplikasikan dua kali, hasilnya kembali ke keadaan awal, mirip dengan gerbang X dua kali. Gerbang ini menjadi fondasi dari banyak algoritma kuantum karena efek interferensinya.

## Pengukuran Qubit : Melihat Tanpa Mengetahui Semua
Ketika kita mengukur qubit dalam basis komputasi (basis 0 dan 1), dengan probabilitas berdasarkan amplitudo :
- Probabilitas dapat hasil 0 = $|α|²$
- Probabilitas dapat hasil 1 = $|β|²$

Namun, setelah diukur, informasi tentang superposisi (α dan β) hilang sepenuhnya. Jadi, tidak mungkin mengetahui nilai α dan β secara pasti hanya melalui pengukuran – inilah salah satu batasan fundamental dalam dunia kuantum.

## Gerbang Kuantum Umum : Matriks Uniter
Semua gerbang kuantum diwakili oleh matriks uniter – yaitu matriks yang tidak mengubah panjang (norma) dari vektor input. Ini penting karena menjaga agar total probabilitas dari hasil pengukuran tetap 1. Contoh:
- Gerbang Identitas yang tidak mengubah qubit
- Gerbang Rotasi yang memutar keadaan qubit dalam ruang kompleks

## Pauli Gates : X, Y, dan Z
Selain gerbang X, ada dua gerbang lain yang dinamakan berdasarkan fisikawan Pauli:
- Gerbang Y : Mengubah $∣0⟩$ menjadi $i∣1⟩$ , dan $∣1⟩$ menjadi $-i∣0⟩$
- Gerbang Z : Mengubah $∣1⟩$ menjadi $-∣1⟩$, tapi $∣0⟩$ tetap

Gerbang-gerbang ini memperluas “pergerakan” dalam ruang kuantum dan memungkinkan lebih banyak manipulasi terhadap informasi.
## Controlled-NOT (CNOT) : Interaksi Antar Qubit
CNOT adalah gerbang dua qubit, yang membuat qubit “**berinteraksi**” :
- Jika qubit kontrol adalah $∣1⟩$, maka target dibalik.
- Jika qubit kontrol adalah $∣0⟩$, maka target tidak berubah

contoh :
- $∣10⟩ → ∣11⟩$ (target dibalik karena kontrol 1)
- $∣11⟩ → ∣10⟩$

Dengan kombinasi gerbang H dan CNOT, kita bisa menghasilkan  "***Entangled state***" seperti $(∣00⟩ + ∣11⟩)/√2$ yang tidak bisa dijelaskan secara klasik, dan menjadi fondasi banyak keajaiban kuantum seperti teelportasi dan kriptografi kuantum.

### NOTE :
Materi ini menunjukan bahwa meskipun banyak istilah dan operasi dalam komputasi kuantum terasa teknis dan matematis, intinya adalah tentang bagaimana kita bisa memanipulasi dan emmbaca informasi kuantum secara hati hati. Dengan alat seperti Gerbang Hadamard, CNOT, dan pegukuran kuantum, kita bisa memulai membangun sistem komputasi yang sangat kuat namun sangat berbeda dari komputer klasik. komputasi kuantum bukan hanya tentang kecepatan, tetapi juga tentang cara berpikir dan beroperasi dengan hal yang benar benar baru.

## *Catatan PART 2*

> ### CNOT (Controlled–NOT)
- Gerbang 2‑qubit: qubit #1 (kontrol), #2 (target).
- Jika kontrol = 1, target dibalik; jika 0, target tetap; → menghasilkan korelasi yang kuat.

> ### Entanglement & Bell State
Sebuah sirkuit sederhana:

```
|0⟩──H──■───
           │
|0⟩──────⊕───
```

H pada qubit pertama lalu CNOT → menghasilkan entangled pair:


**catatan:** “Jika tahu hasil qubit A, langsung tahu B. Itulah ‘bahasa rahasia’ quantum.”

> ### Universalitas

Kombinasi gerbang satu‑qubit (X, H, Rθ, dst.) + CNOT → mampu merepresentasikan setiap unitary pada multi-qubit → ini adalah **quantum universality**.

> ### Model Sirkuit Quantum

Tiga fase dasar:

1. **Inisiasi**: set qubit ke |0⟩.
2. **Komputasi**: jalankan sequence gerbang.
3. **Pengukuran**: baca hasil, probabilitas sesuai |α|².

<br>
<br>

# PART 3 :Komputasi Kuantum Universal (Universal Kuantum Komputing)
## Apa Itu Komputasi Kuantum Universal?
Komputer Kuantum sebagai alat paling potensial untuk mensimulasikan sistem fisik apapun. Berbeda dari komputer biasa yang bekerja berdasarkan logika klasik, komputer kuantum bekerja dengan memanfaatkan hukum fisika kuantum. Ini memungkinkan pemrosesan informasi yang jauh lebih kompleks.

## Model Dasar Komputasi Komputasi Kuantum 
Sebuah komputasi kuantum terdiri dari 3 langkah utama :
1. memulai dari keadaan awal : Biasanya menggunakan sususnan qubit seperti $|0000⟩$.
2. Menerapkan rangkaian gerbang kuantum : Menggunakan gerbang seperti Hadamard, rotasi, dan CNOT.
3. Melakukan pengukuran : Untuk Mendapatkan hasil akhir berdasarkan probabilitas amplitudo kuantum.

meskipun langkah-langkahnya tampak sederhana, efek yang bisa dihasilkan sangat dalam dan kompleks.


**jika kita ibaratkan komputer klasik itu seperti puzzle 2D, maka logika kuantum seperti menyusun puzzle 3D yang berubah bentuk setiap kali disentuh.**

## Apakah Perlu Menguasai Semua Model?
Walaupun ada banyak model lain seperti *measurement-based quantum computation* atau *topological quantum computation*, semuanya sebenarnya bisa dikonversi ke model dasar rangkaian kuantum. Ini seperti berbagai bahasa pemrograman yang berbeda tapi tetep bisa di convert ke logika dasar "0" dan "1".

## Fase Global 
Gerbang tertentu hanya mengubah “fase” suatu qubit, misalnya mengalikannya dengan nilai seperti $eiθ$. Ini disebut fase global. Yang menarik, perubahan ini tidak mempengaruhi hasil pengukuran. Jadi, walaupun secara matematis terjadi perubahan, komputer kuantum mengabaikannya dalam praktik.

## Kuantum vs Komputasi Klasik

Seperti kapal yang bisa menyebrangi laut lebih cepat daripada berjalan didarat, komputer kuantum bisa menyelesaikan masalah tertentu jauh lebih cepat daripada komputer biasa.  
Namun, untuk bisa setara komputer klasik, **komputer kuantum harus mampu meniru rangkaian logika klasik**, termasuk gerbang AND dan NOT.  
**Solusi** dari permasalahan tersebut menggunakan gerbang ***Toffoli***, yaitu gerbang 3 qubit yang bisa meniru logika AND. ini menjadi jembatan antara dunia klasik dan kuantum.

## Kegunaan Nyata Komputer Kuantum

### 1. Simulasi Sistem Kuantum
Inilah aplikasi paling menjanjikan dimana **komputer kuantum dapat meniru perilaku molekul atau atom** dalam sekala besar. Misalnya dalam dunia farmasi, ini bisa mengubah proses penemuan obat dari hitungan tahun menjadi jam atau menit.  
Namun masalahnya, Simulasi sistem kuantum butuh jumlah data yang sangat besar misalnya 2ⁿ amplitudo untuk n qubit. Komputer biasanya tak sanggup menyimpan dan mengolah datanya.  
**Komputer kuantum dapat menanganinya** hanya dengan menambahkan beberapa qubit untuk mensimulasikan lebih banyak atom. 
### 2. Algoritma Cepat
Contoh paling terkenal adalah **algoritma Shor** untuk faktorisasi bilangan besar. Ini bisa digunakan untuk **membobol sistem enkripsi** yang digunakan bank dan layanan email saat ini.  
Karena hal tersebut banyak lembaga intelejen mendanai riset komputasi kuantum sejak tahun 1990-an.

## Apakah Komputer Kuantum Bisa Meniru Semua sistem Fisik?
Komputer klasik sulit untuk mensimulasikan sistem kuantum. Tapi apakah komputer kuantum bisa meniru semua sistem fisik, seperti relativitas umum dan gravitasi kuantum?  
Hal tersebut masih mejadi misteri. Kita belum memiliki teori final untuk menyatukan semua hukum fisika, terutama untuk gravitasi kuantum.  
Namun, untuk simulasi teori medan kuantum (bagian dari Standard Model), sudah ada kemajuan besar. Beberapa makalah dari John Preskill menunjukkan bahwa komputer kuantum bisa menyimulasinya dengan efisien, meski belum secara penuh.  
## Lingkaran Ajaib Fisika dan Komputasi
    Hukum fisika menentukan jenis komputasi yang bisa kita lakukan, namun komputasi juga bisa digunakan untuk memahami hukum fisika itu sendiri

Inilah “loop ajaib” yang membuat dunia ini begitu dapat dimengerti. Kita bisa merancang mesin berdasarkan hukum alam, dan mesin itu kembali digunakan untuk menyelidiki alam semesta.
## Komputasi Kuantum dan Masa Depan
Komputer kuantum bukan hanya alat yang lebih cepat. Ia juga membuka cara baru dalam memahami dan mengendalikan materi tingkat paling dasar. Jika teknologi berkembang pesat, kita bisa memasuki era di mana materi dapat diprogram, seperti kita memprogram perangkat lunak saat ini.

## *Catatan PART 3*

> ### Pengukuran & Probabilitas

* Pada pengukuran `|ψ⟩ = α|0⟩+β|1⟩` → hasil 0 dengan probabilitas |α|², 1 dengan |β|². State setelah pengukuran menjadi basis yang dipilih.

> ### Fase: Global vs Lokal

* **Fase global** tidak memengaruhi hasil pengukuran → tidak berpengaruh.
* **Fase relatif** (φ antara α dan β) sangat penting → menentukan interferensi & efek gerbang.

> ### Simulasi Gerbang Klasik

Gerbang klasik (NOT, AND, OR) dapat dibangun via kombinasi gerbang quantum (contohnya menggunakan Toffoli gate dengan 2 kontrol).

> ### Aplikasi

### Grover's Algorithm (Quantum Search)

* Mempadankan oracle + diffusor → mempercepat pencarian: dari O(N) → O(√N).
* **Diagram**:

  ```
  |ψ⟩──[Oracle]──[Diffusor]──(ulangi O(√N) kali)──┬─Measure
                                                  └─output item
  ```
* **Analog:** seolah‑olah kita “melompat” dekat target lebih cepat dibanding mencari satu per satu biasa.

### Quantum Teleportation

* Gunakan Bell pair + CNOT + H + 2-bit classical → mentransfer state |ψ⟩ meskipun qubit fisiknya berbeda.

<br>
<br>
<br>

---
---
---

<div align="center">
    <h1 style="font-size: 45px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #e63946; background: linear-gradient(45deg, #e63946, #1d3557); -webkit-background-clip: text; color: transparent; padding: 20px 40px; border: 4px solid transparent; border-radius: 12px; background-image: linear-gradient(45deg, #e63946, #1d3557);">
        Quantum Machine Learning Tutorial
    </h1>
</div>

---
---
---

<br>

<br>

# 1. Introduction
Sejak awal revolusi industri, kekuatan komputasi telah menjadi penggerak utama perubahan besar. Awalnya, komputer hanya bisa menghitung, lalu berkembang menjadi mesin yang bisa mengendalikan proses industri, hingga kini mampu mengenali wajah dan menerjemahkan bahasa lewat kecerdasan buatan (AI).

Namun, komputer konvensional seperti CPU dan GPU kini menghadapi batasan fisik: tidak bisa terus diperkuat tanpa batas. Di sinilah komputer kuantum muncul sebagai harapan baru. Komputer ini bekerja berdasarkan prinsip-prinsip fisika kuantum—ilmu yang mempelajari dunia yang sangat kecil, seperti partikel subatom.

Dengan kemampuan unik untuk berada dalam banyak keadaan sekaligus (superposisi) dan saling terhubung walau terpisah (entanglement), komputer kuantum menjanjikan kecepatan pemrosesan yang jauh melampaui komputer biasa.
### Lalu apa itu kuantum machine learning ?
Quantum Machine Learning (QML) adalah gabungan dari dua dunia: komputasi kuantum dan kecerdasan buatan (AI).

Secara sederhana, QML adalah usaha untuk menggunakan komputer kuantum agar dapat menjalankan algoritma-algoritma pembelajaran (machine learning) dengan lebih cepat, efisien, atau lebih baik dibanding cara klasik. Harapannya, QML bisa menyelesaikan tugas-tugas tertentu—misalnya prediksi cuaca, pengenalan suara, hingga pemodelan molekul—dengan hasil yang lebih unggul.

Tiga unsur utama dari QML:

- Quantum Processor: Otak pemroses berbasis mekanika kuantum.

- Tugas yang Spesifik: Misalnya mengenali pola atau menyelesaikan persamaan.

- Keunggulan: Baik dari sisi kecepatan, akurasi, atau efisiensi.
### Komputer Klasik vs Kuantum
![klasik vs kuantum](/Pembelajaran/Quantum-ML/image_QuantumML/klasik-vs-kuantum.png)

Menjelaskan bahwa baik komputer klasik maupun kuantum memiliki struktur umum: ada input (data masuk), proses komputasi, dan output (hasil).
Bedanya:

- Komputer klasik pakai bit (0/1) dan gerbang logika digital.

- Komputer kuantum pakai qubit (superposisi) dan gerbang kuantum (mengatur amplitudo probabilitas).

### Bit vs Qubit
![klasik vs kuantum-1](/Pembelajaran/Quantum-ML/image_QuantumML/Tabel-1_Bit-Vs-Qubit.png)
![klasik vs kuantum-2](/Pembelajaran/Quantum-ML/image_QuantumML/Tabel-2_Bit-Vs-Qubit.png)

- Untuk 3 bit klasik → 8 kemungkinan.

- Untuk 3 qubit → bisa menyimpan dan memproses ke-8 kemungkinan secara bersamaan, dalam satu waktu.

Artinya dengan jumlah qubit yang sama, kapasitas informasi yang dibawa bisa jauh lebih besar daripada bit klasik.
Qubit mematuhi aturan tensor product, bukan perkalian biasa.

### Dimensi Sistem Qubit
$$
Jumlah \ kemungkinan \ sistem \ N \ Qubit = 2^N
$$
Semakin banyak qubit, jumlah keadaan yang bisa direpresentasikan bertambah secara eksponensial.  
Contoh:
- 2 qubit → 4 kemungkinan
- 3 qubit → 8 kemungkinan
- 10 qubit → 1024 kemungkinan

### Kuantum Volume
$$
\log_2(V_Q) = \arg \max_m \min(m, d(m))
$$
Ini adalah cara untuk mengukur kemampuan komputer kuantum secara keseluruhan.

Semakin besar V<sub>Q</sub>, semakin bagus kualitas dan skalabilitas sistem kuantum.

Nilai ini mempertimbangkan berapa banyak qubit dan seberapa dalam rangkaian (circuit) yang bisa diproses dengan benar.

### Empat Sektor QML
![Sektor QML](/Pembelajaran/Quantum-ML/image_QuantumML/Sektro-QML.png)

| Komputasi | Data    | Sektor                                        |
| --------- | ------- | --------------------------------------------- |
| Klasik    | Klasik  | CC (ML biasa)                                 |
| Klasik    | Kuantum | CQ (klasifikasi hasil eksperimen kuantum)     |
| Kuantum   | Klasik  | QC (komputasi kuantum untuk data citra/suara) |
| Kuantum   | Kuantum | QQ (pemrosesan data kuantum asli)             |

Gambar ini menunjukkan bahwa Quantum Machine Learning bisa diterapkan dalam banyak kombinasi — dan tutorial ini fokus pada QC dan QQ, karena di situlah komputasi kuantum benar-benar memberi perbedaan.

### Quantum vs Classical Neural Network
![ANN clasik vs kuantum](/Pembelajaran/Quantum-ML/image_QuantumML/ANN-Clasik-vs-Kuantum.png)
Gambar ini memperlihatkan bahwa:

Baik jaringan neural klasik maupun kuantum memiliki input → hidden layers → output.
Bedanya:
- Model klasik memakai bobot dan fungsi aktivasi.
- Model kuantum memakai gerbang kuantum dan ukurannya berupa probabilitas hasil.

### Peta perkembangan QML
![QML mapping 1](/Pembelajaran/Quantum-ML/image_QuantumML/map-QML-1.png)
![QML mapping 2](/Pembelajaran/Quantum-ML/image_QuantumML/map-QML-2.png)

**Gambar 1.3**: Menunjukkan bagaimana algoritma kuantum (seperti HHL dan QSVT) memberikan kecepatan lebih tinggi dibanding algoritma klasik.  

**Gambar 1.5**: Membandingkan kemampuan model kuantum dalam tiga aspek:
- **Expressivity**: Seberapa banyak pola yang bisa dipelajari.
- **Trainability**: Seberapa mudah dilatih (konvergensi).
- **Generalization**: Seberapa baik hasil pelatihan bisa diterapkan ke data baru.
# 2. Basic of Quantum Komputing
## 2.1 Dari Bit Klasik ke Qubit
Bit klasik hanya bisa bernilai 0 atau 1, sedangkan Qubit bisa dalam keadaan 0, 1, atau gabungan keduanya. Jika diibaratkan, Bit seperti saklar lampu hanya ON (1) atau OFF (0).Sedangkan qubit seperti gelombang cahaya: bisa berada di banyak tempat dalam satu waktu, berkat fenomena superposisi.
### Representasi Qubit
$$ ∣ψ⟩=α∣0⟩+β∣1⟩ $$
dengan
$$ ∣α∣^2 + ∣β∣^2 = 1 $$

- Qubit tidak hanya 0 dan 1, tapi gabungan dari keduanya.
- α dan β adalah angka kompleks (bisa dianggap sebagai "bobot"), dan jika dikuadratkan lalu dijumlahkan hasilnya harus 1
- Qubit seperti probabilitas "mengambang", jadi ketika diukur, hasilnya hanya 0 atau 1, tapi sebelumnya dia bisa "campuran" keduanya.

### Bola Bloch (Bloch Sphere)
![QUBIT-VISUALITATION](/Pembelajaran/Quantum-ML/image_QuantumML/qubit_visualisation.png)

Lingkaran 3D (mirip bola dunia) yang menunjukkan semua posisi kemungkinan dari satu qubit.
Titik kutub utara mewakili ∣0⟩, kutub selatan ∣1⟩, dan semua titik lain di permukaan bola adalah keadaan superposisi.

ini adalah cara memvisualisasikan semua keadaan mungkin dari satu qubit dalam ruang 3 dimensi  
semakin tinggi kompleksitas posisi di bola, semakin rumit keadaan kuantumnya  
Rotasi bola mewakili transformasi qubit, seperti operasi dalam sirkuit kuantum.

### Basis dan Notasi Dirac
- Basis Standar
$$∣0⟩ = \begin{bmatrix}1 \\ 0\end{bmatrix}, ∣1⟩ = \begin{bmatrix}0 \\ 1\end{bmatrix}$$

- Qubit
$$ ψ⟩=α \begin{bmatrix}1 \\ 0\end{bmatrix} + β \begin{bmatrix}0 \\ 1\end{bmatrix} = \begin{bmatrix}α \\ β\end{bmatrix}$$

> ### **Referensi:**

- [Quantum Computing](https://quantum.country/qcvc)
- [Quantum Machine Learning Tutorial](https://qml-tutorial.github.io/)