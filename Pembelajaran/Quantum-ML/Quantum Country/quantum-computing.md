
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

Qubit juga tidak sekadar angka. Ia direpresentasikan sebagai vektor dua dimensi, yaitu arah di dalam ruang yang disebut *state space* (ruang keadaan). Dua arah paling dasar adalah :

- $|0⟩$ → vektor $[1, 0]$ , seperti  bit 0.
- $|1⟩$ → vektor $[0, 1]$ , seperti  bit 0.  
  
Namun qubit bisa berada di antara keduanya, misalnya dalam keadaan : $0.6|0⟩ + 0.8|1⟩$, yang secara visual seperti panah yang condong ke arah tertentu antara dua ujung.

## Visualisasi Qubit
![QUBIT-VISUALITATION](../image_QML/qubit_visualisation.png)

Untuk membantu membayangkan, bayangkan sebuah bola transparan. Setiap posisi pada permukaan bola ini bisa mewakili satu keadaan qubit. Arah panah di permukaan bola menunjukkan seperti apa “campuran” dari 0 dan 1 dalam qubit.  

Jika panah mengarah tepat ke atas, itu artinya keadaan 0 ($|0⟩$). Jika mengarah ke bawah, itu keadaan 1 ($|1⟩$). Dan arah lainnya menggambarkan campuran probabilitas antara keduanya.

## Superposisi : Lebih dari sekedar 0 dan 1
Superposisi adalah konsep yang membuat qubit unik. Ia bisa berada dalam "campuran" dari 0 dan 1, dan baru akan "memilih salah satu" saat kamu melihatnya (diukur). Jadi, selama belum diukur, dia menyimpan potensi jawaban ganda. Keadaan campuran seperti $0.6|0⟩ + 0.8|1⟩$ disebut superposisi.

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
Kita tidak bisa menyimpan panjang $α$ atau $β$ secara presisi. Measurement hanya mengungkap 0 atau 1, dan setelahnya amplitudo hilang, jadi tidak bisa menyimpan informasi tak terbatas.

> ### Visualisasi dengan Bloch Sphere
Qubit dapat divisualisasikan sebagai titik di permukaan bola Bloch :
- Sudut $θ$ menentukan probabilitas (dekat kutub $Z$ → probabilitas besar ke 0 atau 1).
- Sudut $φ$ menyangkut fase kompleks.
- Rotasi pada sphere sebanding dengan penerapan gerbang. Misalnya $X$ memutar 180° di sumbu $X$.

![Bloch Sphere – Geometric Representation of Quantum State](../image_QML/geometric-of-quantum-state.jpeg)

> ### Sekilas mengenai Gerbang Dasar (Unitaritas)
- **$X$ (NOT)** : menukar $|0⟩$ ↔ $|1⟩$ yang berfungsi sebagai kliniskan

$$
X = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

- **$H$ (Hadamard)** : mengonversi basis ke superposisi, contoh: 

$$ 
H|0⟩ = (|0⟩+|1⟩)/√2. 
$$

- Semua gerbang adalah *unitary* → preserve panjang vektor → $U†U = I$.
- **Analogi** : “Bayangkan memutar panah di Bloch Sphere. Nah, itulah yang dilakukan gerbang quantum.”

<br>
<br>

# PART 2 : Gerbang Logika Kuantum (*quantum logic gates*)

## Apa Itu Gerbang Logika Kuantum?
Gerbang logika kuantum adalah cara untuk memanipulasi informasi kuantum, yaitu keadaan dari qubit (unit terkecil dalam komputasi kuantum). Konsep ini mirip dengan gerbang logika dalam komputer klasik (seperti AND, OR, NOT), tetapi bekerja berdasarkan prinsip mekanika kuantum. Gerbang-gerbang ini menjadi fondasi semua perhitungan dalam komputer kuantum, memungkinkan operasi seperti teleportasi kuantum hingga algoritma kuantum yang kompleks.

## Gerbang NOT Kuantum : Gerbang $X$
Gerbang NOT dalam dunia kuantum disebut juga sebagai **gerbang $X$**. Ia bekerja dengan membalik Qubit.
- Jika input adalah $∣0⟩$ maka hasilnya $∣1⟩$
- Jika input adalah $∣1⟩$ maka hasilnya $∣0⟩$

Untuk superposisi seperti $α∣0⟩ + β∣1⟩$, gerbang $X$ akan menukar posisi amplitudonya menjadi $α∣1⟩ + β∣0⟩$. Dalam representasi matriks, gerbang X ditulis sebagai :

$$
X = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

Dalam diagram sirkuit kuantum, gerbang ini digambarkan sebagai kotak bertuliskan “$X$” yang terletak di atas garis waktu qubit.

## Quantum Wire (Kabel Kuantum)
Dalam konteks **komputasi kuantum**, *quantum wire* bukan hanya sekadar kawat fisik berukuran nano. Ia merupakan **komponen konseptual dalam sirkuit kuantum** yang menunjukkan **aliran informasi kuantum dari satu titik ke titik lain**. Dengan kata lain, *quantum wire* adalah **jalur evolusi waktu dari sebuah qubit**.

### 1. Representasi dalam Sirkuit Kuantum
Dalam diagram sirkuit kuantum (*quantum circuit diagram*), *quantum wire* digambarkan sebagai **garis horizontal** yang menghubungkan gerbang-gerbang kuantum. Setiap wire mewakili satu **qubit**, dan arah ke kanan menunjukkan evolusi waktu. Berikut contoh sederhananya :

```
|0⟩───H───●───X───
          │
        ──X───────
```

Di sini,

* Garis horizontal adalah **quantum wire**.
* Simbol `|0⟩` menunjukkan keadaan awal qubit.
* Simbol `H` , `X` , `●` , dll adalah **gerbang kuantum (*quantum gates*)**.
* *Quantum wire* menghubungkan gerbang ini dan menunjukkan bahwa qubit yang sama mengalami transformasi berurutan.

### 2. Makna Fisik Quantum Wire
Secara fisik, qubit dapat diimplementasikan sebagai :

* **Foton yang berjalan dalam serat optik** atau dalam interferometer.
* **Ion terperangkap** yang dipindahkan oleh medan elektromagnetik.
* **Superkonduktor** dengan aliran arus Josephson.

Dalam semua implementasi ini, quantum wire bisa berarti **jalur fisik yang dilalui qubit** *atau* sekadar **representasi logis** dari qubit yang diteruskan dari satu gerbang ke gerbang lainnya.

### 3. Tantangan
Meskipun wire tampak pasif, sebenarnya **menjaga informasi kuantum tetap stabil saat mengalir dalam *wire*** adalah tantangan besar. Masalah-masalah utama meliputi:

* **Dekohesi (*decoherence*)** : Qubit bisa kehilangan informasi karena gangguan dari lingkungan.
* **Noise kuantum** : Gangguan acak yang bisa mempengaruhi hasil akhir komputasi.
* ***Loss*** : Pada sistem berbasis foton, qubit bisa hilang selama proses propagasi.

Maka, banyak penelitian diarahkan untuk merancang *quantum wire* yang:

* Meminimalkan interferensi,
* Mengurangi kehilangan energi atau informasi,
* Dan mampu mempertahankan superposisi serta keterikatan (*entanglement*).

### 4. Penerapan dan Analogi
Dalam sistem kuantum nyata :

* Di **komputer kuantum optik**, *quantum wire* adalah jalur cahaya melalui interferometer.
* Di **komputer kuantum berbasis superkonduktor**, *quantum wire* adalah saluran microwave yang menghubungkan qubit dan resonator.
* Dalam **logika kuantum linear**, qubit bisa mengalir dari satu modul ke modul lain seperti gelombang, dan *wire* merepresentasikan lintasan mereka.

## Sirkuit Dua Gerbang $X$ : Identitas
Menempatkan dua gerbang $X$ secara berurutan akan mengembalikan qubit ke kondisi semula. Ini serupa dengan membalikkan koin dua kali. Secara matematis :

$$
X(X(α∣0⟩ + β∣1⟩)) = α∣0⟩ + β∣1⟩
$$

Secara matriks, ini berarti perkalian dua matriks $X$ menghasilkan matriks identitas (tidak mengubah apapun).

## Gerbang Hadamard ($H$) : Campuran Unik
Gerbang Hadamard ($H$) adalah gerbang kuantum pertama yang memperlihatkan perilaku unik dunia kuantum. Ia menciptakan superposisi dari keadaan dasar :

- $H∣0⟩ = \frac{(∣0⟩ + ∣1⟩)}{√2}$, artinya qubit berada ditengah tengah antara 0 dan 1.

<br>

- $H∣1⟩ = \frac{(∣0⟩ - ∣1⟩)}{√2}$

Jika diaplikasikan dua kali, hasilnya kembali ke keadaan awal, mirip dengan gerbang $X$ dua kali. Gerbang ini menjadi fondasi dari banyak algoritma kuantum karena efek interferensinya.

## Pengukuran Qubit : Melihat Tanpa Mengetahui Semua
Ketika kita mengukur qubit dalam basis komputasi (basis 0 dan 1), dengan probabilitas berdasarkan amplitudo :
- Probabilitas dapat hasil 0 = $|α|²$
- Probabilitas dapat hasil 1 = $|β|²$

Namun, setelah diukur, informasi tentang superposisi ($α$ dan $β$) hilang sepenuhnya. Jadi, tidak mungkin mengetahui nilai $α$ dan $β$ secara pasti hanya melalui pengukuran. Inilah salah satu batasan fundamental dalam dunia kuantum.

## Gerbang Kuantum Umum : Matriks Uniter
Semua gerbang kuantum diwakili oleh matriks uniter, yaitu matriks yang tidak mengubah panjang (norma) dari vektor input. Ini penting karena menjaga agar total probabilitas dari hasil pengukuran tetap 1. Contoh:
- Gerbang Identitas yang tidak mengubah qubit
- Gerbang Rotasi yang memutar keadaan qubit dalam ruang kompleks

## Pauli Gates : $X$, $Y$, dan $Z$
Selain gerbang $X$, ada dua gerbang lain yang dinamakan berdasarkan fisikawan Pauli :

- Gerbang $Y$ : Mengubah $∣0⟩$ menjadi $i∣1⟩$ , dan $∣1⟩$ menjadi $-i∣0⟩$
- Gerbang $Z$ : Mengubah $∣1⟩$ menjadi $-∣1⟩$, tapi $∣0⟩$ tetap

Gerbang-gerbang ini memperluas “pergerakan” dalam ruang kuantum dan memungkinkan lebih banyak manipulasi terhadap informasi.
## Controlled-NOT ($CNOT$) : Interaksi Antar Qubit
$CNOT$ adalah gerbang dua qubit, yang membuat qubit “**berinteraksi**” :
- Jika qubit kontrol adalah $∣1⟩$, maka target dibalik.
- Jika qubit kontrol adalah $∣0⟩$, maka target tidak berubah

contoh :
- $∣10⟩ → ∣11⟩$ (target dibalik karena kontrol 1)
- $∣11⟩ → ∣10⟩$

Dengan kombinasi gerbang $H$ dan $CNOT$, kita bisa menghasilkan  "***Entangled state***" seperti,

$$
(∣00⟩ + ∣11⟩)/√2
$$

yang tidak bisa dijelaskan secara klasik dan menjadi fondasi banyak keajaiban kuantum seperti teelportasi dan kriptografi kuantum.

### NOTE :
Materi ini menunjukan bahwa meskipun banyak istilah dan operasi dalam komputasi kuantum terasa teknis dan matematis, intinya adalah tentang bagaimana kita bisa memanipulasi dan membaca informasi kuantum secara hati hati. Dengan alat seperti Gerbang $H$, $CNOT$, dan pegukuran kuantum, kita bisa memulai membangun sistem komputasi yang sangat kuat namun sangat berbeda dari komputer klasik. Komputasi kuantum bukan hanya tentang kecepatan, tetapi juga tentang cara berpikir dan beroperasi dengan hal yang benar benar baru.

## *Catatan PART 2*

> ### $CNOT$ (Controlled–NOT)
- Gerbang 2‑qubit : qubit #1 (kontrol), #2 (target).
- Jika kontrol = 1, target dibalik; jika 0, target tetap; → menghasilkan korelasi yang kuat.

> ### *Entanglement* & *Bell State*
Sebuah sirkuit sederhana :

```
|0⟩──H──■───
           │
|0⟩──────⊕───
```

$H$ pada qubit pertama lalu $CNOT$ → menghasilkan *entangled pair* :


**catatan:** “Jika tahu hasil qubit A, langsung tahu B. Itulah ‘bahasa rahasia’ quantum.”

> ### Universalitas
Kombinasi gerbang satu‑qubit ($X$, $H$, $Rθ$, dst.) + $CNOT$ → mampu merepresentasikan setiap unitary pada multi-qubit → ini adalah ***quantum universality***.

> ### Model Sirkuit Quantum
Tiga fase dasar :

1. **Inisiasi** : set qubit ke $|0⟩$.
2. **Komputasi** : jalankan sequence gerbang.
3. **Pengukuran** : baca hasil, probabilitas sesuai $|α|²$.

<br>
<br>

# PART 3 :Komputasi Kuantum Universal (Universal Kuantum Komputing)

## Apa Itu Komputasi Kuantum Universal?
Komputer Kuantum sebagai alat paling potensial untuk mensimulasikan sistem fisik apapun. Berbeda dari komputer biasa yang bekerja berdasarkan logika klasik, komputer kuantum bekerja dengan memanfaatkan hukum fisika kuantum. Ini memungkinkan pemrosesan informasi yang jauh lebih kompleks.

## Model Dasar Komputasi Komputasi Kuantum 
Sebuah komputasi kuantum terdiri dari 3 langkah utama :
1. memulai dari keadaan awal<br>Biasanya menggunakan sususnan qubit seperti $|0000⟩$.

2. Menerapkan rangkaian gerbang kuantum<br>Menggunakan gerbang seperti Hadamard, rotasi, dan $CNOT$.

3. Melakukan pengukuran<br>Untuk Mendapatkan hasil akhir berdasarkan probabilitas amplitudo kuantum.

Meskipun langkah-langkahnya tampak sederhana, efek yang bisa dihasilkan sangat dalam dan kompleks.

**jika kita ibaratkan komputer klasik itu seperti puzzle 2D, maka logika kuantum seperti menyusun puzzle 3D yang berubah bentuk setiap kali disentuh.**

## Apakah Perlu Menguasai Semua Model?
Walaupun ada banyak model lain seperti *measurement-based quantum computation* atau *topological quantum computation*, semuanya sebenarnya bisa dikonversi ke model dasar rangkaian kuantum. Ini seperti berbagai bahasa pemrograman yang berbeda tapi tetep bisa di convert ke logika dasar "0" dan "1".

## Fase Global 
Gerbang tertentu hanya mengubah “fase” suatu qubit, misalnya mengalikannya dengan nilai seperti $e^{i\theta}$. Ini disebut fase global. Yang menarik, perubahan ini tidak mempengaruhi hasil pengukuran. Jadi, walaupun secara matematis terjadi perubahan, komputer kuantum mengabaikannya dalam praktik.

## Kuantum vs Komputasi Klasik

Seperti kapal yang bisa menyebrangi laut lebih cepat daripada berjalan didarat, komputer kuantum bisa menyelesaikan masalah tertentu jauh lebih cepat daripada komputer biasa.  
Namun, untuk bisa setara komputer klasik, **komputer kuantum harus mampu meniru rangkaian logika klasik**, termasuk gerbang AND dan NOT.  

**Solusi** dari permasalahan tersebut menggunakan gerbang ***Toffoli***, yaitu gerbang 3 qubit yang bisa meniru logika AND. ini menjadi jembatan antara dunia klasik dan kuantum.

## Kegunaan Nyata Komputer Kuantum

### 1. Simulasi Sistem Kuantum
Inilah aplikasi paling menjanjikan dimana **komputer kuantum dapat meniru perilaku molekul atau atom** dalam sekala besar. Misalnya dalam dunia farmasi, ini bisa mengubah proses penemuan obat dari hitungan tahun menjadi jam atau menit.  

Namun masalahnya, Simulasi sistem kuantum butuh jumlah data yang sangat besar misalnya $2ⁿ$ amplitudo untuk $n$ qubit. Komputer biasanya tak sanggup menyimpan dan mengolah datanya. 

**Komputer kuantum dapat menanganinya** hanya dengan menambahkan beberapa qubit untuk mensimulasikan lebih banyak atom. 

### 2. Algoritma Cepat
Contoh paling terkenal adalah **algoritma Shor** untuk faktorisasi bilangan besar. Ini bisa digunakan untuk **membobol sistem enkripsi** yang digunakan bank dan layanan email saat ini.  

Karena hal tersebut banyak lembaga intelejen mendanai riset komputasi kuantum sejak tahun 1990-an.

## Apakah Komputer Kuantum Bisa Meniru Semua sistem Fisik?
Komputer klasik sulit untuk mensimulasikan sistem kuantum. Tapi apakah komputer kuantum bisa meniru semua sistem fisik, seperti relativitas umum dan gravitasi kuantum?  

Hal tersebut masih mejadi misteri. Kita belum memiliki teori final untuk menyatukan semua hukum fisika, terutama untuk gravitasi kuantum.

Namun, untuk simulasi teori medan kuantum (bagian dari Standard Model), sudah ada kemajuan besar. Beberapa makalah dari *John Preskill* menunjukkan bahwa komputer kuantum bisa menyimulasinya dengan efisien, meski belum secara penuh.  

## Lingkaran Ajaib Fisika dan Komputasi
Hukum fisika menentukan jenis komputasi yang bisa kita lakukan, namun komputasi juga bisa digunakan untuk memahami hukum fisika itu sendiri.

Inilah “loop ajaib” yang membuat dunia ini begitu dapat dimengerti. Kita bisa merancang mesin berdasarkan hukum alam, dan mesin itu kembali digunakan untuk menyelidiki alam semesta.

## Komputasi Kuantum dan Masa Depan
Komputer kuantum bukan hanya alat yang lebih cepat. Ia juga membuka cara baru dalam memahami dan mengendalikan materi tingkat paling dasar. Jika teknologi berkembang pesat, kita bisa memasuki era di mana materi dapat diprogram, seperti kita memprogram perangkat lunak saat ini.

## *Catatan PART 3*

> ### Pengukuran & Probabilitas

* Pada pengukuran `|ψ⟩ = α|0⟩+β|1⟩` → hasil 0 dengan probabilitas $|α|²$, 1 dengan $|β|²$. State setelah pengukuran menjadi basis yang dipilih.

> ### Fase: Global vs Lokal

* **Fase global** tidak memengaruhi hasil pengukuran → tidak berpengaruh.
* **Fase relatif** ($φ$ antara $α$ dan $β$) sangat penting → menentukan interferensi & efek gerbang.

> ### Simulasi Gerbang Klasik

Gerbang klasik (NOT, AND, OR) dapat dibangun via kombinasi gerbang quantum (contohnya menggunakan Toffoli gate dengan 2 kontrol).

> ### Aplikasi

### Grover's Algorithm (Quantum Search)

* Mempadankan oracle + diffusor → mempercepat pencarian: dari $O(N) → O(√N)$.
* **Diagram** :

  ```
  |ψ⟩──[Oracle]──[Diffusor]──(ulangi O(√N) kali)──┬─Measure
                                                  └─output item
  ```

* **Analogi** : seolah‑olah kita “melompat” dekat target lebih cepat dibanding mencari satu per satu biasa.

### Quantum Teleportation

* Gunakan *Bell pair* + $CNOT$ + $H$ + 2-bit classical → mentransfer state $|ψ⟩$ meskipun qubit fisiknya berbeda.

<br>
<br>
<br>

---

> ### **Referensi:**

- [Quantum Computing](https://quantum.country/qcvc)