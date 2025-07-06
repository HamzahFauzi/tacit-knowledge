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
## Quantum Machine Learning Tutorial

Isi di sini...

> ### **Referensi:**

- [Quantum Computing](https://quantum.country/qcvc)
- [Quantum Machine Learning Tutorial](https://qml-tutorial.github.io/)