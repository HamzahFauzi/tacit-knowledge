# Tutorial BoltzTraP2 Quantum Espresso
Panduan sederhana penggunaan BoltzTraP2 untuk menghitung sifat termoelektrik dengan data dari Quantum Espresso (QE). Tutorial ini dilakukan dengan menggunakan linux dan BoltzTraP2 versi 25.3.1 untuk mensimulasikan data termoelektrik.

## Daftar Isi
- [Requirements](#requirements)
- [Instalasi Environment](#instalasi-environment)
- [Langkah Perhitungan](#langkah-perhitungan)
   1. [Relaksasi](#1-relaksasi-struktur)
   2. [SCF]()
   3. [NSCF]()
   4. [Interpolasi dengan BoltzTraP2]()
   5. [Integrasi Transport Properties]()
   6. [Plot Hasil]()
- [Bahan Bacaan]()

## Requirements
- **Quantum Espresso**
- **Python environment**
    - `cython`
    - `matplotlib`
    - `numpy`
    - `cmake`
    - `boltztrap2`
    - `pyfftw vtk`
    - `scienceplots`

## Instalasi Environment
Ada beberapa cara untuk membuat Python environment (venv, anaconda, atau lainnya), silahkan gunakan metode yang paling Anda kuasai.

### Contoh instalasi venv:
`python -m venv /path/to/new/virtual/environment`
```
python -m venv .venv    
source btpenv/bin/activate
```
Selanjutnya install module lainnya.
```
pip install cython
pip install matplotlib
pip install numpy
pip install cmake
pip install bolztrap2
pip install pyfftw vtk
pip install scienceplots
```
> *cython dan cmake diperlukan untuk instalasi boltztrap2*

Atau bisa diinstall semua secara langsung.
```
pip install pyfftw vtkpip install numpy matplotlib cython cmake boltztrap2 pyfftw vtk scienceplots
```
Untuk memeriksa instalasi dapat menggunakan `pip list`. Untuk melihat cython dan bolztrap2 juga dapat menggunakan `btp2 -V` dan `cython -V`.

## Langkah Perhitungan
> *Contoh perhitungan akan menggunakan material mos2*
### 1. Relaksasi Struktur
Jika posisi atom belum optimal, lakukan relax di QE.

```
pw.x < mos2.relax.in > mos2.relax.out
```

Gunakan posisi akhir `mos2.relax.out` untuk input SCF.

### 2. buat scf

### 3. buat nscf

### 4. interpolate

### 5. integrate

### 6. plot menggunakan python
bisa menggunakan .py atau .ipynb sesuai selera.

## Bahan Bacaan
- [TU Wien BoltzTraP2 Page](https://www.tuwien.at/en/tch/tc/theoretical-materials-chemistry/boltztrap2)
- [BoltzTraP2 Official Wiki](https://gitlab.com/sousaw/BoltzTraP2/-/wikis/home)
- [BoltzTraP2 Tutorial](https://youtube.com/playlist?list=PLIRLJRX4ncIXlRXa4_J9CCVFGpYFTJFX3&si=yWmF60mFWHgpUsO6) by Edi Suprayoga
- [Si example & qe2boltz2.py](https://drive.google.com/file/d/100QL0jntBT6bS088lLfi_jIR1uPZJJ4L/view?usp=sharing) from BoltzTraP2 Tutorial

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*