# Mini Project 2  

Praktikum Dasar Dasar Pemrograman  
Sistem Manajemen Kepanitiaan Makrab FT 25  

Nama : Az-Zahra Imsawati Sugianto  
NIM : 2509116062  
Kelas : Sistem Informasi B'25  

# Flowchart Sistem Manajemen Kepanitiaan Makrab FT 25  
<img width="3542" height="1843" alt="Flowchart_minpro2" src="https://github.com/user-attachments/assets/9fa6f592-adbe-4ce7-9eca-cbe659e2deb2" />  

  
# Menu Utama (Menu Login)  
<img width="476" height="145" alt="menu utama" src="https://github.com/user-attachments/assets/b159c934-5f93-4a64-882b-0317c4e33a90" />  

Pada menu ini akan menampilkan 3 pilihan kepada pengguna yaitu :  
1. Login ketua : Pada menu ini hanya ketua yang dapat mengakses menu ini.
2. Login Panitia : Pada menu ini semua jabatan dan divisi dapat mengakses menu ini dengan password sebagai panitia, pada menu ini akan menampilkan semua data panitia dan pada menu ini digunakan untuk mengubah status tugas panitia makrab.
3. Keluar : Pada menu ini digunakan untuk keluar dari program.
   
<img width="416" height="162" alt="Screenshot 2025-09-28 203320" src="https://github.com/user-attachments/assets/28e7dbdf-c72b-47eb-81ef-438255036054" />  

Apabila input diluar menu maka akan muncul "Pilihan Tidak Valid".

# 1. Login Ketua  
<img width="410" height="239" alt="Screenshot 2025-09-28 203752" src="https://github.com/user-attachments/assets/54812862-e8dd-4868-b116-177689fffb5e" />  

Tampilan awal ketika memilih menu login, user diminta untuk melakukan input username beserta password yang benar, apabila input username dan password yang salah maka akan menampilkan output "Login gagal"  

<img width="296" height="184" alt="Screenshot 2025-09-28 204413" src="https://github.com/user-attachments/assets/1a351317-9550-48fd-b10e-1e8895c6520f" />  

Apabila login berhasil maka akan masuk ke menu ketua. Akan ada 5 menu yaitu :  
1. Tambah Panitia : Menu ini berfungsi untuk ketua menambahkan data kepanitiaan.
2. Lihat Semua Panitia : Jika memilih menu ini maka akan menampilkan data panitia yang sebelumnya telah diinput.
3. Hapus Panitia : Apabila ingin menghapus data, maka pilih menu hapus panitia.
4. Tambah Tugas Panitia : Pada menu ini ialah menu untuk update, yaitu untuk menambah tugas panitia.
5. Keluar : Jika ingin keluar pilih menu ke 5.

<img width="364" height="165" alt="Screenshot 2025-09-28 205424" src="https://github.com/user-attachments/assets/51c2ee32-f2c4-4b81-8cc7-fb36591bc6bb" />  

Jika ketua memilih menu 1 maka akan diminta untuk input ID panitia, nama, jabatan, divisi atau jabatan, dan tugas. Jika data valid maka akan menghasilkan output "Panitia berhasil ditambahkan". Apabila menggunakan ID yang telah digunakan maka output akan muncul "ID sudah digunakan", jika data kosong maka akan muncul "Semua data harus diisi", dan apabila input divisi yang tidak yang tidak ada di daftar maka akan memunculkan output "Divisi atau jabatan tidak valid".  

<img width="416" height="557" alt="Screenshot 2025-09-28 210609" src="https://github.com/user-attachments/assets/71a0f5c7-cf82-4d7a-9711-bb91eeb7bce4" />  

Apabila ketua memilih menu 2 maka akan memunculkan semua data panitia yang telah diinput ketua.  

<img width="265" height="63" alt="Screenshot 2025-09-28 215141" src="https://github.com/user-attachments/assets/1158eab4-9359-48cd-9e5b-8dfb756b5320" />  

Apabila ketua belum memasukan data maka akan memberikan output "Belum ada data panitia".  

<img width="647" height="154" alt="Screenshot 2025-09-28 211224" src="https://github.com/user-attachments/assets/86322d5c-e2ad-4fa5-8d95-776324d7ad58" />  

Apabila ketua ingin menghapus atau mengeluarkan anggotanya, maka pilih menu ke 3. Pada menu ini cara untuk menghapus yaitu input ID beserta alasannya. Apabila ID ditemukan maka akan memunculkan output seperti gambar diatas, bila ID tidak ditemukan maka akan memunculkan output "ID tidak ditemukan"  

<img width="390" height="106" alt="Screenshot 2025-09-28 211852" src="https://github.com/user-attachments/assets/69907b0c-2c60-4356-bd37-68092160e1c4" />  

Pada menu ke 4 ketua dapat menambahkan tugas dan tugas baru akan masuk ke data.  

Apabila ingin kembali ke menu utama pilih 5 (keluar) dan akan langsung menampilkan menu utama.  

# 2. Login panitia  
<img width="472" height="382" alt="Screenshot 2025-09-28 213132" src="https://github.com/user-attachments/assets/b64aa50b-7a65-4743-9397-abd73cc8545c" />  

Pada menu ini yang pertama kali dilakukan setelah memilih 2 atau login panitia adalah input nama beserta password (password untuk panitia khusus). Untuk nama harus terdaftar pada input ketua. Lalu akan menampilkan data semua panitia yang telah diinput oleh ketua.  

<img width="482" height="173" alt="Screenshot 2025-09-28 213733" src="https://github.com/user-attachments/assets/2f58d8d2-e1fd-4d58-9c6c-0a0b0f8d5473" />  

Lalu akan menampilkan apakah kamu ingin konfirmasi tugas? jika iya maka ketik "y" dan pilih tugas yang ingin kamu ubah statusnya. Jika valid maka akan memunculkan output "Status tugas diperbarui". Lalu jika kamu tidak ingin konfirmasi atau ubah status maka ketik "n", maka kamu akan otomatis ke menu utama.  

<img width="524" height="127" alt="Screenshot 2025-09-28 214227" src="https://github.com/user-attachments/assets/6f48771e-f35c-46fe-9a54-2deb4178741a" />  

Apabila input selain angka maka outputnya akan menampilkan seperti gambar diatas.  

# 3. Keluar
<img width="445" height="153" alt="Screenshot 2025-09-28 214658" src="https://github.com/user-attachments/assets/9bb9c359-0b91-472e-a8cc-87d4d651ab75" />  

Jika kamu pilih 3 di menu utama maka kamu akan keluar dari sistem. 



























