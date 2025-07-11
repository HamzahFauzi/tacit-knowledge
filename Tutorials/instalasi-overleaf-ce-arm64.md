# ✅ Tutorial memasang Overleaf CE (Community Edition) pada arsitektur arm64 (Raspberry Pi)

## 🧭 Daftar Isi
- [🛠️ Langkah 1: Mempersiapkan Sistem](#langkah-1-mempersiapkan-sistem)
- [💾 Langkah 2: Clone Overleaf source code (monorepo)](#langkah-2-clone-overleaf-source-code-monorepo)
- [📡 Langkah 3: Build image base sharelatex-base untuk ARM64](#langkah-3-build-image-base-sharelatex-base-untuk-arm64)
- [🔌 Langkah 4: Build image utama sharelatex](#langkah-4-build-image-utama-sharelatex)
- [🔐 Langkah 5: Clone Overleaf Toolkit](#langkah-5-clone-overleaf-toolkit)
- [👥 Langkah 6: Inisialisasi konfigurasi Toolkit](#langkah-6-inisialisasi-konfigurasi-toolkit)
- [🔑 Langkah 7: Tag hasil build agar cocok dengan toolkit](#langkah-7-tag-hasil-build-agar-cocok-dengan-toolkit)
- [⚙️ Langkah 8: Menjalankan Overleaf](#langkah-8-menjalankan-overleaf)
- [🧩 Langkah 9: Mengakses pada browser](#langkah-9-mengakses-pada-browser)
- [🛠️ Langkah 10: Konfigurasi Tambahan](#langkah-10-konfigurasi-tambahan)
- [📚 Bahan Bacaan](#bahan-bacaan)

## Langkah 1: Mempersiapkan Sistem
1. Perangkat Raspberry Pi
2. Device lain dengan arsitektur aarch64
3. Sistem operasi linux (Debian, Ubuntu, atau Arch)
4. Menjalakan perintah berikut ini untuk memperbarui linux:
   ```bash
   sudo apt update && sudo apt upgrade
   ```
5. Memasang docker:
   ```bash
   sudo apt install git curl unzip docker.io docker-compose
   ```
5. Memastikan docker telah aktif:
    ```bash
   sudo systemctl enable docker
   sudo systemctl start docker
   ```

## Langkah 2: Clone Overleaf source code (monorepo)
1. Melakukan clone pada repositori overleaf:
    ```bash
    git clone https://github.com/overleaf/overleaf.git ~/overleaf
    ```

## Langkah 3: Build image base sharelatex-base untuk ARM64
1. Melakukan Build image base ``sharelatex-base`` untuk ARM64:
    ```bash
    sudo env DOCKER_BUILDKIT=1 docker build -t sharelatex/sharelatex-base -f server-ce/Dockerfile-base .
    ```

## Langkah 4: Build image utama sharelatex
1. Melakukan Build image base ``sharelatex``:
    ```bash
    sudo env DOCKER_BUILDKIT=1 docker build -t sharelatex/sharelatex -f server-ce/Dockerfile .
    ```

## Langkah 5: Clone Overleaf Toolkit
1. Melakukan Clone Overleaf Toolkit:
    ```bash
    git clone https://github.com/overleaf/toolkit.git ~/overleaf-toolkit
    ```
2. Meninjau struktur folder Overleaf Toolkit:
    ```bash
    ls -l
    ```
    Seharusnya menunjukkan seperti ini
    ```bash
    bin
    CHANGELOG.md
    config
    data
    doc
    lib
    LICENSE
    README.md
    ```

## Langkah 6: Inisialisasi konfigurasi Toolkit
1. Melakukan inisialisasi konfigurasi Toolkit:
    ```bash
    sudo ./bin/init
    ```
    Ketika melihat isi pada folder `config/` akan muncul:
    ```bash
    ls config
        overleaf.rc     variables.env     version
    ```
    - overleaf.rc: berkas konfigurasi tingkat atas utama
    - variables.env: variabel lingkungan yang dimuat ke dalam kontainer docker
    - version: versi image docker yang akan digunakan
2. Cek versi yang digunakan:
    ```bash
    cat config/version
    ```

## Langkah 7: Tag hasil build agar cocok dengan toolkit
1. Melakukan Tag hasil build agar cocok dengan toolkit:
    ```bash
    sudo docker tag sharelatex/sharelatex sharelatex/sharelatex:5.5.2
    ```
    Sesuaikan versi `sharelatex:x.x.x`. Gunakan veri yang muncul pada langkah 6 bagian 2.

## Langkah 8: Menjalankan Overleaf
1. Masuk ke dalam folder `overlefa-toolkit`:
    ```bash
    cd ~/overleaf-toolkit
    ```
2. menjalakan perintah:
    ```bash
    sudo ./bin/up
    ```

## Langkah 9: Mengakses pada browser
1. Membuka http://localhost/launchpad atau pada jaringan lokal http://<ip-device>.
2. Pada http://localhost/launchpad akan menampilkan tampilan awal konfigurasi admin.
3. Jika sedang tidak menggunakan device raspberrynya langsung (menggunakan SSH) maka ada konfigurasi yang perlu di atur.

## Langkah 10: Konfigurasi Tambahan
1. Mematikan overleaf dengan perintah:
    ```bash
    sudo ./bin/down
    ```
2. Pada folder `config/` terdapat fie `overleaf.rc`
3. Mengubah bagian:
    ```bash
    OVERLEAF_LISTEN_IP=127.0.0.0 ---> 0.0.0.0
    ```
4. Menjalankan overleaf dengan:
    ```bash
    sudo ./bin/up
    ```
## Bahan Bacaan
- [Dokumentasi Overleaf Toolkit](https://github.com/overleaf/toolkit.git)

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*
