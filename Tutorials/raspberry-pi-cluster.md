# 🚀 Tutorial: Cara Clustering Raspberry Pi 5

Tutorial ini memandu kamu untuk membangun klaster komputasi mini menggunakan Raspberry Pi 5, lengkap dengan Network File System (NFS) untuk berbagi file, Network Information Service (NIS) untuk autentikasi pengguna terpusat, dan Slurm Workload Manager untuk manajemen pekerjaan. Klaster ini terdiri dari satu server (💻 qupi0) dan dua klien (🔗 qupi1, qupi2).

## 🧭 Daftar Isi
- [📦 Prasyarat](#prasyarat)
- [🛠️ Langkah 1: Menyiapkan Sistem Operasi](#langkah-1-menyiapkan-sistem-operasi)
- [💾 Langkah 2: Memasang MicroSD ke Raspberry Pi](#langkah-2-memasang-microsd-ke-raspberry-pi)
- [📡 Langkah 3: Mengatur NFS di qupi0 (Server)](#langkah-3-mengatur-nfs-di-qupi0-server)
- [🔌 Langkah 4: Mengatur NFS di qupi1 dan qupi2 (Klien)](#langkah-4-mengatur-nfs-di-qupi1-dan-qupi2-klien)
- [🔐 Langkah 5: Mengatur NIS di qupi0 (Server)](#langkah-5-mengatur-nis-di-qupi0-server)
- [👥 Langkah 6: Mengatur NIS di qupi1 dan qupi2 (Klien)](#langkah-6-mengatur-nis-di-qupi1-dan-qupi2-klien)
- [🔑 Langkah 7: Mengatur SSH dan Sudoers](#langkah-7-mengatur-ssh-dan-sudoers)
- [⚙️ Langkah 8: Mengatur SLURM](#langkah-8-slurm)
- [🧩 Langkah 9: konfigurasi SLURM](#langkah-9-konfirgurasi-slurm)
- [📚 Bahan Bacaan](#referensi)

## Prasyarat
- ✅ 3x Raspberry Pi 5 (qupi0, qupi1, qupi2).
- ✅ microSD 128GB/256GB (masing-masing Raspberry Pi).
- ✅ Switch/router + kabel LAN.
- ✅ Laptop/komputer untuk konfigurasi awal.
- ✅ Internet aktif.

## Langkah 1: Menyiapkan Sistem Operasi
1. **Unduh dan instal Raspberry Pi Imager** di laptop/komputer dari [situs resmi Raspberry Pi](https://www.raspberrypi.com/software/).
2. **Pasang kartu microSD** (128GB atau 256GB) ke laptop.
3. **Buka Raspberry Pi Imager** dan lakukan konfigurasi:
   - Pilih model Raspberry Pi (pilih "Raspberry Pi 5").
   - Pilih sistem operasi (disarankan Raspberry Pi OS 64-bit untuk performa optimal).
   - Pilih kartu microSD yang terdeteksi di laptop.
4. **Jalankan instalasi** untuk mem-flash OS ke microSD. Tunggu hingga selesai.

## Langkah 2: Memasang MicroSD ke Raspberry Pi
1. **Cabut microSD** dari laptop setelah instalasi selesai.
2. **Pasang microSD** ke slot masing-masing Raspberry Pi 5.
3. Nyalakan setiap Raspberry Pi dan pastikan booting dengan benar.

## Langkah 3: Mengatur NFS di qupi0 (Server)
1. **Instal autofs** di qupi0 untuk mengelola mount otomatis:
   ```bash
   sudo apt update
   sudo apt install autofs
   ```
2. **Atur izin direktori `/qupi`** untuk berbagi file:
   ```bash
   sudo chmod 775 /qupi
   sudo chgrp users /qupi
   sudo chown -R root:users /qupi
   ```

## Langkah 4: Mengatur NFS di qupi1 dan qupi2 (Klien)
1. **Edit file `/etc/auto.master`** di qupi1 dan qupi2:
   ```bash
   sudo nano /etc/auto.master
   ```
   Tambahkan baris berikut di akhir file:
   ```
   /-    /etc/auto.mount
   ```
   Simpan dan keluar (Ctrl+O, Enter, Ctrl+X).

2. **Buat file `/etc/auto.mount`** di qupi1 dan qupi2:
   ```bash
   sudo nano /etc/auto.mount
   ```
   Tambahkan konfigurasi berikut:
   ```
   /qupi    -fstype=nfs,rw    qupi0:/qupi
   ```
   Simpan dan keluar. (Catatan: Ini akan membuat folder `/qupi` otomatis dengan tipe NFS.)

3. **Restart autofs** di qupi1 dan qupi2:
   ```bash
   sudo systemctl restart autofs
   ```

4. **Verifikasi NFS**:
   - Periksa apakah folder `/qupi` muncul di qupi1 dan qupi2.
   - Uji dengan membuat file baru di `/qupi` dari qupi1 atau qupi2 dan pastikan terlihat di qupi0.

## Langkah 5: Mengatur NIS di qupi0 (Server)
1. **Instal NIS** di qupi0:
   ```bash
   sudo apt install nis
   ```

2. **Edit `/etc/default/nis`** untuk memastikan qupi0 bertindak sebagai server:
   ```bash
   sudo nano /etc/default/nis
   ```
   Pastikan tidak ada pengaturan yang menonaktifkan NIS server.

3. **Konfigurasi `/etc/ypserv.securenets`**:
   ```bash
   sudo nano /etc/ypserv.securenets
   ```
   Komentari baris "PLEASE ADJUST" dengan tanda `#` dan tambahkan:
   ```
   255.255.255.0    192.168.1.0
   ```
   Simpan dan keluar.

4. **Buat atau edit `/etc/defaultdomain`**:
   ```bash
   sudo nano /etc/defaultdomain
   ```
   Tambahkan:
   ```
   qupi
   ```
   Simpan dan keluar.

5. **Restart layanan NIS**:
   ```bash
   sudo systemctl restart rpcbind ypserv yppasswdd ypxfrd
   sudo systemctl enable rpcbind ypserv yppasswdd ypxfrd
   ```

6. **Inisialisasi NIS**:
   ```bash
   sudo /usr/lib/yp/ypinit -m
   ```
   Tekan Ctrl+D saat diminta.

## Langkah 6: Mengatur NIS di qupi1 dan qupi2 (Klien)
1. **Instal NIS** di qupi1 dan qupi2:
   ```bash
   sudo apt install nis
   ```

2. **Edit `/etc/yp.conf`**:
   ```bash
   sudo nano /etc/yp.conf
   ```
   Komentari baris yang menyebutkan "yp server" dengan `#`, lalu tambahkan:
   ```
   domain qupi server qupi0
   ```
   Simpan dan keluar.

3. **Edit `/etc/nsswitch.conf`**:
   ```bash
   sudo nano /etc/nsswitch.conf
   ```
   Untuk baris `passwd`, `group`, dan `shadow`, ubah menjadi:
   ```
   passwd: files nis
   group: files nis
   shadow: files nis
   ```
   Simpan dan keluar.

4. **Edit `/etc/defaultdomain`**:
   ```bash
   sudo nano /etc/defaultdomain
   ```
   Tambahkan:
   ```
   qupi
   ```
   Simpan dan keluar.

5. **Restart layanan NIS**:
   ```bash
   sudo systemctl restart rpcbind nscd ypbind
   sudo systemctl enable rpcbind ypbind
   ```

6. **Uji login**:
   - Coba login dengan pengguna yang dibuat di qupi0 untuk memastikan NIS berfungsi.

## Langkah 7: Mengatur SSH dan Sudoers
1. **Periksa pengguna dengan hak sudo**:
   ```bash
   cat /etc/group | grep sudo
   ```

2. **Tambahkan pengguna ke grup sudo** (contoh pengguna: `fufufafa`):
   ```bash
   sudo usermod -aG sudo fufufafa
   ```

3. **Konfigurasi SSH key**:
   - Tambahkan kunci publik ke `authorized_keys` di qupi0:
     ```bash
     cat qupikey.pub >> ~/.ssh/authorized_keys
     ```

4. **Buat SSH key untuk akses antar node**:
   - Dari qupi1 atau qupi2, buat kunci SSH:
     ```bash
     ssh-keygen -t rsa
     ```
   - Salin kunci publik ke qupi0:
     ```bash
     ssh-copy-id mainadmin@10.10.216.30
     ```
## Langkah 8: Slurm
Qupi0 = login node
Qupi1 qupi2 = compute nodes
membuat ```config``` seperti di quasi6
membuat folder ```/scratch``` di root untuk seluruh nodes di qupi0,qupi1,qupi2
### resume
qupi0
```/qupi/config```
```/scratch```
qupi1 dan qupi2
```/scratch```

1. **Setting munge**
   ```sudo passwd root``` untuk password
   ```su``` hingga ada tanda #
   - Buat MUNGE key dan atur hak aksesnya:
     ```bash
     dd if=/dev/random bs=1 count=1024 > /etc/munge/munge.key
     chown munge:munge /etc/munge/munge.key
     chmod 400 /etc/munge/munge.key
     ```
   - Restart munge:
     ```bash
     systemctl restart munge
     ```
   - Cek munge dapat bekerja pada head node
     ```bash
     munge -n
     ```
   - Juga cek kebalikannya
     ```bash
     munge -n | unmunge
     remunge
     ```
2. Install slurm
   ```bash
   apt install slurm-wlm slurm-wlm-doc slurm-client
   ```
4. Lakukan di qupi1 dan qupi2 aktifkan superuser
   ```bash
   sudo passwd root dengan password quantum
   apt install libmunge-dev libmunge2 munge
   ```
5. lakukan ini untuk superuser untuk qupi1 dan qupi2
   ```bash
   echo "d /var/log/munge 0700 munge munge -" >> /etc/tmpfiles.d/vardirs.conf
   echo "d /var/lib/munge 0700 munge munge -" >> /etc/tmpfiles.d/vardirs.conf
   ```
6. lakukan pada qupi0
   ```bash
   cp /etc/munge/munge.key /qupi/config\
   ``` agar bisa diakses qupi1 dan qupi2
   ```bash
   chown munge:munge munge.key
   chmod 400 munge.key
   ```
7. Balik ke qupi1 dan qupi2
   `/etc/munge` harus diisi oleh `munge.key` dari `/qupi/config`
   ```bash
   su
   cp /qupi/config/munge.key /etc/munge
   ```
   - lakukan `apt install slurm`
8. sebagai mulyono(qupi0) lakukan tutorial ganti ip address dengan qupi1
   ```bash
   munge -n | ssh qupi1 unmunge
   ```
   lakukan di user lain jika error
   ``` bash
   cd /var/yp/
   sudo make
   ```
## Langkah 9: konfigurasi SLURM
1. membuat file konfigurasi
   ```
   mkdir /opt/slurm
   touch /opt/slurm/slurm.conf
   echo "include /opt/slurm/slurm.conf" > /etc/slurm/slurm.conf
   echo "include /opt/slurm/slurm.conf" > /image/pi4/etc/slurm/slurm.conf
   ```
2. Mengunjungi laman
   kofigurator SLURM (https://slurm.schedmd.com/configurator.html)

   
## Bahan Bacaan
- [Dokumentasi Raspberry Pi](https://www.raspberrypi.com/documentation/)

---
*Kembali ke [Daftar Tutorial](https://github.com/BRIN-Q/tacit-knowledge)*
