# Tutorial Clustering Pada Raspberry Pi 5
Langkah pertama
1. Install raspberry pi imager
2. Pasang micro sd 128gb dan 256gb
3. Aplikasi dibuka memilih 3 pilihan, 
    Pilihan 1. pilih sesuai model raspberry (respberry pi 4)
    pilihan 2. pilih operasi sistem (64 bit/32 bit)
    pilihan 3. pilih micro sd yang telah dipasangkan di laptop
4. Lakukan installasi 
Langkah kedua
1. Cabut micro sd di laptop 
2. Pasangkan micro sd di raspberry pi

Langkah selanjutnya installasi qupi0
1.   install `sudo apt install aoutofs` lakukan disemua qupi
2.   memastikan permission di qupi0 `sudo chmod 775`
3.   ganti `root` menajdi `user` dengan `chgrp users /qupi` pilihan kedua `chown-R root:users /qupi`

Langkah pada Qupi1 dan 
1. Beri perintah `sudo nano /etc/auto.master`
2. '/-    /etc/auto.mount' lakukan pada Qupi 2 juga dan save
3. Membuat file baru `sudo nano /etc/auto.mount` dan letakkan konfigurasinya
   ISI KONFIGURASI
   '/qupi    -fstipe=nfs,rw    qupi0:/qupi' (auto fs akan membuat folder baru di etc dengan tipe nfs) lakukan juga di qupi 1 dan 2 isinya sama
4. Resrat autofs pada qupi1 dan qupi2 `sudo sistemctl restart autofs`
5. Cek kembali pada qupi1 dan qupi2 apakah ada folder qupi dan bisa di buka serta bisa menambah file barunya

Langkah selanjutnya
Bagaimana cara membuat user pada qupi0 (server) bisa di akses di qupi1 dan qupi2 (klient)
1. install `sudo apt install nis`
2. buka `sudo nano /etc/default/nis` pastikan tidak ada nis server
3. `sudo nano /etc/ypserv.securenets`
   EDIT BAGIAN PALING BAWAH
   berikan tanda # pada "PLEASE ADJUST"
   255.255.255.0     192.168.1.0
   dan save
4. `sudo nano /etc/defaultdomain` jika tidak ada, maka buat folder sendiri `sudo nano /etc/defaultdomain`
5. lakukan `sudo systemctl restart rpcbind ypservyppasswdd ypxfrd` diulang
6. restart dan ganti ke enable
7. `sudo /usr/lib/yp/ypinit -m` jika sudah ctrl d

Pada Qupi1 dan Qupi2
1. `sudo apt install nis`
2. `sudo nano /etc/yp.conf`
   EDIT BAGIAN BAWAH
   '#'pada yp server
   domain qupi server qupi0 (bikin baru)
3. `sudo nano etc/nsswutch.conf`
   EDIT PASSWD, GROUP, SHADOW
   `files nis`
   dan di save

4. `sudo nano /etc/defaultdomain`
   EDIT
   qupi
6. lalu restart `sudo systemctl restart rpcbind nscd ypbind`
7. lakukan enable `sudo systemctl enable rpcbind ypbind`
8. kemudian login

Cara check yang menjadi sudoer
`cat etc/group | grep sudo`
Cra menambahkan sudoer
`sudo usermod -aG sudo fufufafa`

qupikey.pub harus di autorize `cat qupikey.pup >> authorized_key

Cara membuat keygan
1. `ssh mianadmin@10.10.216.30` salah satu cara untuk mendaparkan ssh
2. `cd/clusterfs/skel` untuk mengeshare file
3. sesuaikan sudo.... yang telah di ambil dari quasi6, lakukan di qupi0
4. 

