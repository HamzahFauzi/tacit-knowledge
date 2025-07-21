# Tutorial BoltzTraP2 Quantum Espresso

WORK IN PROGRESS

Panduan penggunaan BoltzTraP2 di Quantum Espresso. Tutorial ini dilakukan dengan menggunakan BoltzTraP2 versi 25.3.1 untuk mensimulasikan data termoelektrik.

## Daftar Isi
-
-

## alat dan bahan
- python environment
- cython
- numpy
- cmake
- boltztrap2
- pyfftw vtk

## prosedur penginstallan
1. Create python environment. Ada beberapa cara untuk membuat environment python, cukup gunakan cara yang sudah terbiasa. Python environment seharusnya sudah memiliki numpy and matplotlib. type `pip show numpy` atau `pip show matplotlib` untuk melihat apakah numpy dan matplotlib sudah ada. Jika belum, install dengan
```
pip install numpy
pip install matplotlib
```
Jika sudah install bahan lainnya menggunakan `pip install`
```
pip install cython
pip install cmake
pip install bolztrap2
pip install pyfftw vtk
```
Untuk mengecek apakah terinstall dapat menggunakan `pip list`. Untuk melihat cython dan bolztrap2 juga dapat menggunakan `btp2 -V` atau `cython -V`.

## 1. relaksasi
lakukan rileks jika posisi belum teroptimisasi.

## 2. buat scf

## 3. buat nscf

## 4. interpolate

## 5. integrate

## 6. plot menggunakan python
bisa menggunakan .py atau .ipynb sesuai selera.

## Bahan Bacaan
- [TU Wien BoltzTraP2 Page](https://www.tuwien.at/en/tch/tc/theoretical-materials-chemistry/boltztrap2)
- [BoltzTraP2 Official Wiki](https://gitlab.com/sousaw/BoltzTraP2/-/wikis/home)
- [qe2boltz Git](https://github.com/sylwiagutowska/qe2boltz)

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*