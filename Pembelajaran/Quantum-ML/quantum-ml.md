## Quantum Computing

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

## Catatan PART 1

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

## Catatan PART 2

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

# PART 3 :


<br>
<br>

## Quantum Machine Learning Tutorial

Isi di sini...

> ### **Referensi:**

- [Quantum Computing](https://quantum.country/qcvc)
- [Quantum Machine Learning Tutorial](https://qml-tutorial.github.io/)