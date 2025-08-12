# Tutorial BoltzTraP2 Quantum Espresso
Panduan sederhana penggunaan BoltzTraP2 untuk menghitung sifat termoelektrik dengan data dari Quantum ESPRESSO (QE). Tutorial ini dilakukan dengan menggunakan linux dan BoltzTraP2 versi 25.3.1 untuk mensimulasikan data termoelektrik.

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
Jika enviroment berhasil teraktivasi akan terlihat seperti ini:
```
(.venv) user@machine:~$
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
Jika posisi atom belum optimal, lakukan relaksasi di QE menggunakan relax atau vc-relax.

```
&CONTROL
    calculation = 'vc-relax',
    prefix      = 'mos2',
    outdir      = './out',
    pseudo_dir  = '../../pseudo',
    verbosity   = 'high',
    etot_conv_thr = 1.0D-5,
    forc_conv_thr = 1.0D-4,
/

&SYSTEM
    ibrav   = 4,
    a       = 3.17,
    c       = 18.3800404,
    nat     = 3,
    ntyp    = 2,
    ecutwfc = 60.0,
    occupations = 'smearing',
    smearing = 'mv',
    degauss = 1.00000e-02,
/

&ELECTRONS
    conv_thr    = 1.0d-9,
    mixing_beta = 0.7,
/

&IONS
    ion_dynamics = 'bfgs',
/

&CELL
    cell_dynamics = 'bfgs',
    press_conv_thr = 0.5,
    cell_dofree = '2Dxy'
/

ATOMIC_SPECIES
    Mo  95.95   Mo_ONCV_PBE-1.2.upf
    S   32.065  S_ONCV_PBE-1.2.upf

ATOMIC_POSITIONS (crystal)
S   0.6666737055    0.3333474111    0.5470922642
Mo  0.3333405889    0.6666811779    0.4999990000 
S   0.6666737055    0.3333484111    0.4529067358

K_POINTS automatic
    12 12 1 0 0 0
```

```
pw.x < mos2.relax.in > mos2.relax.out
```

Gunakan posisi akhir `mos2.relax.out` untuk input SCF.

### 2. scf

> **file mos2.relax.out**
```
.
.
.
CELL_PARAMETERS (alat=  5.99043182)
   1.004559258   0.000000000   0.000000000
  -0.502279629   0.869973662   0.000000000
   0.000000000   0.000000000   5.798120000

ATOMIC_POSITIONS (crystal)
S             0.6666737103        0.3333474208        0.5851103931
Mo            0.3333405792        0.6666811586        0.4999990000
S             0.6666737103        0.3333484208        0.4148886069
End final coordinates
.
.
.
```

Setelah dilakukan relax, gunakan posisi akhir tersebut sebagai posisi atom di input file `mos2.scf.in`. Input file dapat dijalankan menggunakan `pw.x`

```
&CONTROL
    calculation = 'scf',
    prefix      = 'mos2',
    outdir      = './out',
    pseudo_dir  = '../../pseudo',
    restart_mode= 'from_scratch',
    verbosity   = 'high',
/

&SYSTEM
    ibrav   = 0,
    celldm(1) = 5.99043182,
    nat     = 3,
    ntyp    = 2,
    ecutwfc = 60.0,
    occupations = 'smearing',
    smearing = 'mv',
    degauss = 1.00000e-02,
/

&ELECTRONS
    conv_thr    = 1.0d-9,
    mixing_beta = 0.7,
/

ATOMIC_SPECIES
    Mo  95.95   Mo_ONCV_PBE-1.2.upf
    S   32.065  S_ONCV_PBE-1.2.upf

CELL_PARAMETERS (alat=  5.99043182)
   1.004559258   0.000000000   0.000000000
  -0.502279629   0.869973662   0.000000000
   0.000000000   0.000000000   5.798120000

ATOMIC_POSITIONS (crystal)
S             0.6666737103        0.3333474208        0.5851103931
Mo            0.3333405792        0.6666811586        0.4999990000
S             0.6666737103        0.3333484208        0.4148886069

K_POINTS (automatic)
    72 72 1 1 1 1
```
```
pw.x < mos2.scf.in > mos2.scf.out
```
Jumlah k-points yang akan digunakan dapat diubah sesuai kebutuhan.
### 3. nscf
Setelah scf dilakukan, selanjutnya jalankan nscf menggunakan `pw.x`.
```
&CONTROL
    calculation = 'nscf',
    prefix      = 'MoS2',
    outdir      = './out',
    pseudo_dir  = '../../pseudo',
    restart_mode= 'from_scratch',
    verbosity   = 'high',
/

&SYSTEM
    ibrav   = 0,
    celldm(1) = 5.99043182,
    nat     = 3,
    ntyp    = 2,
    nbnd    = 60,
    ecutwfc = 60.0,
    occupations = 'smearing',
    smearing = 'mv',
    degauss = 1.00000e-02,
/

&ELECTRONS
    conv_thr    = 1.0d-9,
    mixing_beta = 0.7,
/

ATOMIC_SPECIES
    Mo  95.95   Mo_ONCV_PBE-1.2.upf
    S   32.065  S_ONCV_PBE-1.2.upf

CELL_PARAMETERS (alat=  5.99043182)
   1.004559258   0.000000000   0.000000000
  -0.502279629   0.869973662   0.000000000
   0.000000000   0.000000000   5.798120000

ATOMIC_POSITIONS (crystal)
S             0.6666737103        0.3333474208        0.5851103931
Mo            0.3333405792        0.6666811586        0.4999990000
S             0.6666737103        0.3333484208        0.4148886069

K_POINTS (automatic)
72 72 1 1 1 1
```
```
pw.x < mos2.nscf.in > mos2.nscf.out
```
Jumlah k-points yang akan digunakan dapat diubah sesuai kebutuhan.

### 4. Interpolate
Setelah running nscf berhasil, selanjutnya dapat dilakukan interpolasi. interpolasi dapat dilakukan secara langsung menggunakan btp2 dengan membaca langsung file `.xml` di outdir.
```
btp2 -vv interpolate -m 32 -e -0.1 -E 0.1 ./out
```
Pada contoh ini mos2 tidak bisa di interpolasi langsung dan perlu menggunakan `qe2boltz2.py`. Kodingan python dapat ditemukan [disini](#bahan-bacaan). Tempatkan `qe2boltz2.py` satu lokasi folder yang sama dengan `mos2.nscf.out`, jika sudah lakukan:
```
dos2unix qe2boltz2.py
chmod +x qe2boltz2.py
```
>`dos2unix` mengubah format menjadi Unix. \
`chmod +x` membuat `qe2boltz2.py` menjadi executable.

Setelah itu ambil fermi energy pada `nscf.out`.
```
grep Fermi mos2.nscf.out
```
pada contoh ini Fermi energy yang dihasilkan yaitu 0.3478 ev. Setelah itu, execute `qe2boltz2.py`.
```
python qe2boltz2.py mos2 pw 0.3478 0
```
Setelah selesai, dapat di interpolasi menggunakan `btp2`, namun disini langsung di directory dimana file `.structure` dan `.energy` terbuat setelah langkah sebelumnya.
```
btp2 -vv interpolate -m 32 -e -0.1 -E 0.1 ./
```
>`-vv` akan menampilkan process di terminal secara rinci.\
`-m (nilai)` interpolasi k-grid akan (nilai)x lebih padat.\
`-e (nilai)` : Energi minimum relatif terhadap tingkat Fermi (eV).\
`-E (nilai)` : Energi maksimum relatif terhadap tingkat Fermi (eV).

### 5. Integrate
Setelah di interpolasi, akan terbentuk file `interpolation.bt2` yang dapat digunakan untuk melakukan integrasi. Untuk integrasi, cukup lakukan:
```
btp2 -vv integrate interpolation.bt2 -b 10000 300:900:100
```
Integrasi akan dilakukan pada grid energi dengan 10000 grid, pada rentang temperatur 300K hingga 900K dengan kenaikan 100K.

Setelah integrasi selesai, jika menggunakan `-vv`, terminal akan mengoutputkan refined energy fermi yang mana nilainya perlu dicatat/disimpan. Pada contoh yang dilakukan, nilai refined energy fermi adalah `0.010519576241154516 ev`.

### 6. Plot menggunakan python
bisa menggunakan .py atau .ipynb sesuai selera.

## Bahan Bacaan
- [TU Wien BoltzTraP2 Page](https://www.tuwien.at/en/tch/tc/theoretical-materials-chemistry/boltztrap2)
- [BoltzTraP2 Official Wiki](https://gitlab.com/sousaw/BoltzTraP2/-/wikis/home)
- [BoltzTraP2 Tutorial](https://youtube.com/playlist?list=PLIRLJRX4ncIXlRXa4_J9CCVFGpYFTJFX3&si=yWmF60mFWHgpUsO6) by Edi Suprayoga
- [Si example & qe2boltz2.py](https://drive.google.com/file/d/100QL0jntBT6bS088lLfi_jIR1uPZJJ4L/view?usp=sharing) from BoltzTraP2 Tutorial

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*