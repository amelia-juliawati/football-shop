Untuk mengakses aplikasi PWS yang sudah di-deploy, dapat diklink link berikut : https://amelia-juliawati-footballshop.pbp.cs.ui.ac.id/

**Penjelasan checklist tugas :**

**Step-by-step membuat sebuah proyek Django baru**
1. Membuat repositori baru di Github yang bernama football-shop. 
2. Melakukan cloning ke repositori lokal dan menghubungkan repositori lokal saya agar saya dapat melakukan perubahan di device lokal saya. 
3. Mengaktifkan virtual environment agar proyek saya tidak bertabrakan dengan versi lain yang ada pada komputer saya atau agar lingkungan proyek (package dan dependensi) ini terisolasi. Virtual environment ini akan selalu saya aktifkan setiap kali saya sedang bekerja dengan proyek saya.
4. Mengunduh semua requirement yang dibutuhkan (termasuk django) agar proyek dapat dibuat dengan baik. 
5. Membuat proyek django dengan menjalankan perintah *django-admin startproject football_shop .*. 
6. Membuat beberapa file yang dibutuhkan, seperti file .env dan .env.prod. untuk membuat lingkungan development agar proyek dapat berjalan, baik untuk testing maupun untuk diakses melalui tautan. 
7. Agar proyek saya dapat diakses melalui link yang telah tertera di atas, saya juga membuat proyek baru pada PWS yang penjelasannya dapat dilihat di bawah. 
8. Mengatur bagian settings.py agar proyek dapat berjalan secara lancar dan dapat diakses melalui link di atas. 
9. Menambahkan .gitignore agar Git mengabaikan file privasi dan tidak dimasukkan di GitHub.

**Step-by-step membuat aplikasi dengan nama main**
1. Menjalankan perintah *python manage.py startapp main* yang mengartikan bahwa main (berupa direktori) akan terbentuk dengan file lainnya yang juga telah diberikan sebagai struktur dasar. 
2. Menambahkan *main* sebagai isi dari list INSTALED_APPS yang berada pada settings.py agar Django dapat mengetahui bahwa ada suatu aplikasi bernama main dan aplikasi tersebut dapat diakses. 

**Step-by-step melakukan routing pada proyek**
1. Mengakses file *urls.py* dalam direktori proyek, bukan direktori aplikasi *main*
2. Menambahkan fungsi include dari *django.urls* pada bagian import (bagian atas)
3. Meambahkan rute URL aplikasi *main*, yaitu main.urls dalam list *urlpatterns*. Path diarahkan ke string kosong agar main menjadi halaman utama.

**Step-by-step membuat model pada aplikasi main**
1. Membuka dan mengisi *models.py* yang telah disediakan sebagai file kosong (struktur dasar) pada direktori aplikasi main. Dibuat kelas bernama Product sebagai model. Lalu, dibuat pilihan kategori yang ada. Setelah itu, ditambahkan beberapa atribut yang diminta dan tambahan dengan spesifikasi yang sesuai (misal nilai default atau maksimal huruf). 
2. Membuat migrasi model agar Django dapat melacak perubahan pada model basis data yang saya miliki. Saya menjalankan perintah *python manage.py makemigrations* di terminal untuk menciptakan file migrasi yang berisi perubahan model.
3. Menetapkan migrasi yang sudah dibuat sebelumnya dengan menjalankan perintah *python manage.py migrate* di terminal.

**Step-by-step membuat fungsi pada views.py**
1. Membuat direktori baru, yaitu templates dan membuat file bernama *main.html* yang akan berisi teks yang akan dilihat ketika proyek pertama kali dibuka
2. Menambahkan baris import yang dibutuhkan pada views.py. Saya menambahkan fungsi render untuk menghubungkan view dengan template menggunakan data yang saya masukkan
3. Mengisi file *main.html* dengan teks dan juga sintaks yang diinginkan menggunakan template variables agar dapat menampilkan nilai dari variables pada views.py
4. Membuat fungsi show_main dengan context yang berisi data yang dibutuhkan untuk diperlihatkan di *main.html*

**Step-by-step membuat routing pada urls.py aplikasi main**
1. Membuat file *urls.py* di dalam direktori *main* agar terpisah dari routing proyek utama.
2. Mengisi file *urls.py* dengan import fungsi yang dibutuhkan, mendefinisikan nama untuk main, dan membuat list *urlpatterns* yang berisi pemetaan URL ke fungsi di *views.py*, yaitu show_main agar aplikasi langsung menunjukkan halaman utama

**Step-by-step melakukan deployment ke PWS**
1. Membuka halaman PWS dan login menggunakan SSO
2. Membuat proyek baru dan mengisi project name dengan footballnews
3. Menyimpan informasi mengenai username dan password
4. Menyalin isi file .env.prod untuk kemudian di-paste pada Project Environment Variables. Hal ini dapat dilakukan dengan mengakses tab Environs dan Raw Editor. SCHEMA yang saya gunakan adalah tugas_individu. 
5. Menambahkan URL deployment PWS pada settings.py. Saya menambahkan informasi pada ALLOWED_HOST dengan memasukkan URL saya sesuai dengan format
6. Melakukan git add, commit, dan push agar perubahan dapat tersimpan di GitHub
7. Menjalankan perintah yang tersedia pada Project Command, yaitu untuk remote add pws, membuat branch, dan melakukan push pws master. Setelah itu, proyek sudah dapat diakses pada tautan PWS

**Bagan Request Client ke Web Aplikasi Berbasis Django**
Link gambar bagan : https://drive.google.com/file/d/1GuhQV8q4nPcqB9mLlcMjt2YGM1-1fRNb/view?usp=sharing
* highlight biru = komponen yang digunakan (misal pengguna menggunakan browser) atau dibuat (misal membuat Model menggunakan models.py)
* highlight merah = komponen eksternal atau pihak ketiga

Berdasarkan bagan yang telah dibuat, dapat dilihat alur interaksi pengguna dengan aplikasi. Pertama, pengguna akan mengakses web server, yang kemudian meneruskan request ke WSGI untuk membuka aplikasi web berbasis Django. Setelah itu, akan dilakukan proses URL Resolution, yaitu mencocokkan URL request dari pengguna dengan URL patterns yang ada di Django. Pada tahap ini, *urls.py* berfungsi sebagai alat bantu untuk routing atau mengarahkan request pengguna agar dapat menampilkan halaman yang sesuai dengan *views.py*. Django pertama-tama akan memeriksa *urls.py* pada level proyek untuk menentukan rute yang cocok. Jika ditemukan kecocokan, request akan diteruskan ke *urls.py* level aplikasi (misalnya melalui include()) untuk menampilkan tampilan utama aplikasi. Jika tidak ada kecocokan, Django akan menampilkan error 404 Not Found. Setelah pencocokan URL dengan *urls.py* berhasil, Django akan memanggil *views.py* yang berisi logika aplikasi dan menyiapkan data yang kemudian akan dikirim ke pengguna dengan memanggil *models.py*. *models.py* mendefinisikan struktur data dan berperan sebagai penyedia query interface untuk database yang berfungsi untuk mengambil, menyimpan ataupun memproses data. Setelah data diproses melalui *models.py*, *views.py* akan memanggil template atau file html yang berfungsi sebagai struktur format untuk menampilkan data kepada pengguna. Hasil render template kemudian akan dikembalikan sebagai response ke pengguna. 

**Peran settings.py**

Pada Django, *settings.py* berfungsi sebagai file konfigurasi utama yang mengatur berbagai aspek proyek. Di dalam *settings.py* terdapat informasi tentang koneksi database yang diatur melalui DATABASES, daftar aplikasi yang aktif melalui INSTALLED_APPS (dimana kita dapat memasukkan aplikasi yang telah kita buat, contohnya main), konfigurasi keamanan dan pengaturan global seperti TIME_ZONE dan LANGUAGE_CODE, serta konfigurasi untuk development dan production melalui variabel environment (misalnya .env pada proyek ini). Pada *settings.py* juga terdapat pengaturan routing proyek, sehingga aplikasi dapat diakses melalui URL tertentu, contohnya link PWS yang digunakan pada proyek ini. Tanpa *settings.py*, Django tidak akan mengetahui bagaimana suatu proyek dijalankan dan fitur-fitur penting seperti database, aplikasi, serta routing tidak akan berfungsi dengan benar.

**Cara Kerja Migrasi Database di Django**

Migrasi database adalah suatu mekanisme di Django untuk menyinkronkan setiap perubahan yang dibuat pada *models.py* dengan struktur database sehingga database dapat menyimpan perubahan tersebut. Ketika dijalankan perintah *python manage.py makemigrations* di terminal, Django akan memeriksa semua perubahan yang terjadi pada model. Sesuai dengan namanya, perintah ini akan membuat file migrasi yang berisi perubahan model yang belum diterapkan di database. File ini berisi perintah SQL yang merepresentasikan perubahan tersebut, misalnya membuat tabel baru, menambah kolom, atau mengubah tipe data kolom. Setelah itu, migrasi akan dijalankan dengan menggunakan perintah *python manage.py migrate*. Pada tahap ini, Django akan membaca file migrasi yang telah dibuat sebelumnya untuk kemudian dijalankan atau mengeksekusi perintah SQL di database agar perubahan dapat diterapkan di database. Django juga menyimpan status migrasi yang sudah dijalankan di tabel django_migrations agar dapat diketahui migrasi mana yang sudah diterapkan dan migrasi baru yang perlu dijalankan.

**Alasan Django Dijadikan Framework Permulaan**

Menurut saya, Django merupakan framework yang sangat sesuai sebagai permulaan pembelajaran pengembangan perangkat lunak karena kemudahan yang ditawarkannya bagi pengembang. Django memungkinkan kita untuk mengembangkan suatu aplikasi dengan cepat dikarenakan banyak fitur bawaan yang dapat langsung digunakan, seperti autentikasi, routing, ORM, dan lain-lain. Selain itu, Django menggunakan bahasa pemrograman Python yang cenderung lebih mudah dipahami dan lengkap dibandingkan bahasa lain. Fitur-fitur Python juga dapat langsung dimanfaatkan dalam Django. 

Django bersifat gratis dan open source sehingga memiliki komunitas pengguna yang besar. Hal ini memudahkan pengguna untuk mendapatkan bantuan ketika menghadapi masalah. Selain itu, dengan pola arsitektur MVT dan struktur folder serta file yang mudah dimengerti, Django mempermudah pengguna untuk memahami alur pengerjaan suatu proyek. Django juga unggul dalam hal keamanan dikarenakan sudah memiliki proteksi bawaan sehingga pengembang dapat lebih fokus pada pengembangan aplikasi. Django juga fleksibel untuk pengembangan berbagai jenis proyek karena kompatibel dengan berbagai jenis database dan mampu menangani trafik tinggi pada proyek berskala besar.

**Feedback Asisten Dosen Tutorial 1** : Asisten dosen pada tutorial 1 sudah sangat membantu dan interaktif dengan mahasiswa. Saya merasa sangat terbantu dengan adanya asisten dosen yang tersedia di Discord karena dapat bertanya secara langsung mengenai permasalahan yang saya temui.