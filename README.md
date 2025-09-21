 Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

 Name: Edward Jeremy Worang
 NPM: 2406359475

 **TUGAS 2**

 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 Secara ringkas:

 kita buat repository di github dulu dan buat proyek baru di PWS dengan nama Aplikasi yang unik, dan nanti
 jangan lupa untuk diinit dan isi requirement.txt dependencies untuk mensetup djangonya

Terus kita membuat proyek django baru dengan key word django-admin startproject nama proyekk

Kedua kita membuat aplikasi main, kenapa kita buatnya? Untuk memisahkan domain aplikasi yaitu product
ke dalam app, memudahkan modularitas, testing dan juga reusability menurut saya ini mirip seperti OOP

kita buat Routing proyek dan aplikai produk dengan kata kunci path('', include('main.urls')),
analoginya adalah seperti berikut, 

Routing proyek = mengarahkan kamu dari pintu masuk mall ke toko yang benar.
Routing aplikasi = mengarahkan kamu di dalam toko ke bagian yang kamu cari.

keempat buat model product, sesuai sepesifikasi dari tugas, mirip seperti OOP ketika belajar di DDP1

Kelima migrasi database, kata kunci makemigrations dan migrate, setiap kali kita update DB atau model kita
harus jalankan perintah ini agar bisa direfleksikan kepada web.

Keenam, Views: Buat fungsi show_main(request) yang nanti akan dirender dan kirim datanya contextnya seperrti app_name. Template: Menampilkan data tersebut, kita memisahkan logika yaitu views dan presentasi yaitu template

Ketujuh, kita implementasikan routing apda main/urls.py

Kedelapan, registrasi model Product di main/admin.oy agar data bisa diisi atau diubah lewat
django admin

Terakhir kita lakukan deployment, secara ringkas, kita ambil dulu link dari PWS dimana kita buat proyek kedua kita
terus kita taruh link tersebut di allowed_host agar proyek kita bisa dilihat melalui domain pacil.
Terus setelah semua sudah kelar kita git push di web dan git push ke PWS.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![alt text](20250906_230559.jpg)

Kita mulai dari sisi usernya yaitu ketika melakukan request, misal enter link website kita, terus di django(URL dispatcher) Mendaftar pola URl view mana yang harus dipanggil, ada root urls.py milik proyek yang include urls.app
yaitu milik app main kita.

Tearus lanjut ke views.py, ini menenerima request, memanggil model bila perlu atau juga mempersiapkan
suatu context lalu menrender ke template yang berbasis HTML dalam kasus proyek kita.

Models.py definsi struktur data dan relasi tabel, dimana view bisa memanggil model kita untuk lakukan
query, insert, update, atau delete 

Template HTML, file .html yang dirender oleh view dengan context(data) dan nanti yang akan ditampilkan
kepada user.

3. Jelaskan peran settings.py
settings.py adalah dimana kita konfigurasi proyek, perannya meliputi:
-Daftar app yang aktif pada installed apps variable
-Konfigurasi databases
-Mengatur templates
-Static dan Media settings dimana lokasi file statis dan media
-Allowed Host, debug dan seceret key dimana kita bisa mengaturkan keamanan dan environment
Secara rangkum settings.py mengontrol bagaimana aplikasi berjalan dan berinteraksi dengan lingkungan eksternal

4. Bagaimana cara kerja migrasi database di Django?
Perubahan model (mis. tambah field total_sold) ditulis di models.py.

Jalankan python manage.py makemigrations — Django membuat file migration baru (kode Python yang mendeskripsikan perubahan DB: AddField, CreateModel, dsb.).

Jalankan python manage.py migrate — Django menjalankan operasi-oprasi yang terdapat di migration file pada database aktual.

5. Mengapa Django?
Menurut saya karena Django menyertakan banyak fitur yang membuat pelajar dapat membangun aplikasi nyata cepat
tanoa memilih dan mengintegrasi banyak paket. Terus juga bisa implementasikan struktur yang teroganisir yaitu
MVT template dan juga sebagai tambahan banyak pemula ketika belajar pemrograman mulai dari bahasa python dulu
sehingga django bisa jadi choice yang baik, terus juga komunitas django besar sehingga banyak resources.

6. Semua sudah perfect si, saya harap asisten dosen tetap konsistent dalam pekerjaannya dan juga semangat 
terus untuk mengajar kita (thumbs up).


**TUGAS 3**

1.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Menghubungkan Komponen yang Terpisah, Platform modern biasanya dibangun dengan arsitektur terdistribusi microservices, serverless, dll.. Data delivery memastikan bahwa semua komponen yang terpisah ini dapat saling berkomunikasi dan bertukar data dengan lancar.
-Menyediakan Data Reatime untuk Pengalaman yang Dinamis
Pengguna modern mengharapkan pengalaman yang cepat dan real-time. Data delivery memungkinkan update informasi terjadi tanpa perlu merefresh halaman secara manual.
- Memastikan Keandalan dan Ketahanan Sistem 
Dalam skenario kegagalanm, data delivery yang dirancang dengan baik menggunakan antrian atau message queues dapat menyimpan data sementara sampai sistem tujuan siap memprosesnya kembali. Ini mencegah kehilangan data yang kritis.
- Meningkatkan kemanan data, dalam hal enkripsi data dalam perjalanan yang dapat diakses oleh authorized user only
- Menskala Sistem secara Horizontal 
Data delivery memungkinkan beban kerja didistribusikan ke banyak server atau worker. Ketika lalu lintas data meningkat, platform dapat dengan mudah menambah kapasitas pemrosesan tanpa mengubah arsitektur inti.\

2.  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya si JSON lebih baik karena hal utama yaitu readibility nya sangat jelas dibanding XML karena JSON berstruktur key value pair mirip struktur data ketika DDP 1 jadi sangat realte. Mengapa JSON lebih popular?
JSON jauh lebih ringkas, mudah dibaca, memiliki peforma yang lenih baik karena strukturnya yang sederhana parsing JSON jauh lebih cepat dan menggunakan memori yang lebih sedikit dibandingkan XML, JSON adalah bahasa de facto untuk RESTful APIs. Hampir semua API modern (Twitter, Facebook, Google, dll.) mengembalikan respons dalam format JSON karena kemudahan konsumsinya oleh klien JavaScript di frontend (React, Vue, Angular).

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Berfungsi untuk memvalidasi data yang telah diinput oleh user pada form. Memeriksa apakah semua data yang diinput oleh user biasanya dari request.POST memenuhi semua aturan yang telah didefinisikan di form seperti tipe data, required field, panjang maksimal, dll.

Mengembalikan nilai boolean True jika semua data valid, atau False jika ada yang tidak valid.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan csrf_token  karena Django menggunakan mekanisme ini untuk mempertahankan pertahanan terhadap serangan Cross-Site Request Forgery (CSRF).

Secara sederhana, csrf_token adalah token rahasia yang unik yang dibuat oleh server Django untuk setiap sesi pengguna. Ketika form dikirim token ini juga dikirim kembali. Server kemudian membandingkan token yang diterima dengan token yang dia simpan untuk sesi tersebut jika cocok request diperbolehkan, jika tidakk request ditolak.

Jikda tidak menambahkan token tersebut, Middleware CsrfViewMiddleware akan Menolak Request Django memiliki middleware yang aktif secara default yang memeriksa semua request, Error "403 Forbidden": Ketika middleware tersebut tidak menemukan token CSRF yang valid dalam request POST yang masuk, Django akan secara sengaja menolak request tersebut dan mengembalikan respons HTTP 403 Forbidden

Penyerang dapat melancarkan serangan CSRF misal secara analogi, Bayangkan CSRF seperti seorang penipu yang memalsukan tanda tangan Anda di sebuah formulir transfer bank. Bank yaitu servery hanya melihat formulir yang sudah ditandatangani dan mentransfer uang, tanpa tahu bahwa Anda sebenarnya tidak pernah mengisi formulir itu.

cara kerja penyerang:
Korban login ke sebuah situs web target (misalnya, situs bank di bank.com). Login ini membuat cookie sesi yang valid tersimpan di browser korban.

Penyerang membujuk korban untuk mengunjungi website jahat milik penyerang. Bujukan ini bisa melalui link dalam email, iklan, atau komentar di forum.

Di website jahat tersebut, terdapat elemen tersembunyi yang secara otomatis mengirim request POST ke endpoint penting di bank.com. Request ini bisa berupa perintah untuk transfer uang, mengubah email, atau mengubah password.

source : https://portswigger.net/web-security/csrf

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Tujuan utama dari semua implementasi ini adalah untuk membangun aplikasi web yang lengkap, aman, dan dapat diakses oleh berbagai klien

pertama kita menambahkan views untuk XML dan JSON, Format HTML hanya cocok untuk manusia. Mesin membutuhkan data terstruktur yang mudah diurai, yaitu XML dan JSON . Dengan menyediakan endpoint XML/JSON, kita membuat data aplikasi dapat dikonsumsi oleh berbagai klien, meningkatkan kegunaan dan integrasi jadi kayak backendnya di abstract, jadi user tidak perlu lihat yang compleks tapi final tampilan yaitu dari HTML. Terus ada juga buat index by id untuk JSON dan XML agar kita bisa akses producgt yang specific melalui id mereka.

kedua, membuat routing teripisah untuk setiap view yang ada, Setiap fungsi yang berbeda dalam aplikasi harus memiliki alamat (URL) yang unik sehingga dapat diakses secara spesifik

ketiga memnuat halaman daftar dengan tombol add dan detail itu untuk memberikan user experience dan juga sebagai
fitur untuk tujuan web kita yaitu jual produk kaitan dengan sepak bola, di html ada line seperti a href... sebagai contoh: <a href="{% url 'create_item' %}">Add New Item</a> kita bisa lihat kalau misal user click tombol tersebut
maka django akan cek url berdasarkan kode di html dan jika terdapat di url path maka ia akan execute fungsi di viewss dari url. Halaman detail product itu tentunya kita harus buat template file baru karena struktur dari halamannya beda dan juga programmer lain bisa mudah baca dan tentukan webpage apa yang dia sedang lihat melalui vs code.

keempat, ini menyinggung soal halaman form dan juga beberapa yang sudah dibahas pada step ketiga.  Tugas "menampilkan form" dan "memproses data form" adalah dua tanggung jawab yang berbeda. Memisahkan logika ini membuat kode lebih bersih dan mudah dikelola. Halaman form khusus (create_product.html) hanya fokus pada satu tugas: mengumpulkan input user. View create_product menangani dua hal menampilkan form kosong (GET) dan memproses data yang dikirim (POST) yang nanti akan ditampil ke HTML create product. Pemisahan ini mencegah kekacauan logika.

6. Tidak ada, aman saja.

4 URL postman:
![alt text](<Screenshot 2025-09-14 150642.png>)
![alt text](<Screenshot 2025-09-14 150809.png>)
![alt text](<Screenshot 2025-09-14 150832.png>)
![alt text](<Screenshot 2025-09-14 150936.png>)



**Tugas 4**
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form bawaan Django yang dipakai untuk menangani proses login autentikasi user.
Kelas ini tersedia di django.contrib.auth.forms.AuthenticationForm dan biasanya digunakan bersamaan dengan view bawaan seperti LoginView

kelebihhan:

-Built in  dan siap pakai
Tidak perlu membuat form login manual,  gunakan kelas bawaan saja

-Integrasi penuh dengan sistem auth Django
Validasi langsung memanfaatkan backend autentikasi yang terdaftar.

-Dukungan keamanan: 

Otomatis membersihkan data input.

Menghitung percobaan login gagal bisa digunakan untuk rate-limiting.

Tidak mengekspos detail apakah username atau password yang salah

- dan mudah dipakai dengan login view yang turunan dari django

2.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi, Proses memverifikasi identitas pengguna untuk  memastikan kamu siapa.
Biasanya melalui kombinasi username + password, atau mekanisme lain seperti SS0  siak

cara implementasi, dengan modul django.contrib.auth

Secara ringkas:

Backends  akan menentukan bagaimana user diverifikasidefault cek username and password.

Form bawaan yaitu misalnya AuthenticationForm.

Views bawaan seperti LoginView, LogoutView.

Method  authenticate(request, username= password=) untuk memverifikasi user.

Setelah sukses, Django membuat session untuk menyimpan status login.


Otorisasi (Authorization), Proses menentukan hak akses setelah identitas diverifikasi  memastikan kamu boleh melakukan apa?. Contoh: User biasa boleh membaca artikel, tetapi hanya admin boleh menghapus artikel.

cara implementasi juga gunakan django.contrib.auth,
Permissions seperti  misalnya add_post, change_post, delete_post.

Groups yaitu sekumpulan permissions yang bisa diberikan ke user.

Decorators seperti @login_required, @permission_required('app.permission').

Class-based mixins  LoginRequiredMixin, PermissionRequiredMixin.

Django otomatis membuat permission dasar add, change, delete, dan view untuk setiap model, dan bisa ditambah custom permission.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

dalam konteks menyinpan state web

Kelebihan cookies:
-Disimpan di client dan tidak membenani server
-persisten bisa bertahan mesikpun browser diclose
-Mudah diakses oleh javascript
- dan dapat digunakan lintas servers yang berarti informasi bisa dibawa ke domain lain

Kekurangan cookies:
-Kemananan yang rentan dan mudah diintip atau dicuri
-Ukuran yang terbetas sekitar 4Kb per cookie
-Mudah dimodifikasi oleh client maka tidak cocok untuk menyimpan data sensitif


kelebihan sessions:
- Lebih aman dan mudah diatur, data sensitif tidak dikirim ke client hanya id dan django sudah menyediakan middleware sessiop siap pakai
-lebih fleksible yaitu bisa simpan object kompleks contohnya adalah keranjang belanja
- bisa dimpan di berbagai backend

kekurangan sessions:
-Membebani server maka semakin banyak user, semakin besar data session yang harus disimpan server.

-Perlu manajemen storage maka session lama harus dibersihkan (expired).

-Butuh cookie juga tetap tergantung cookie (untuk menyimpan session ID), jadi kalau cookie dimatikan, session tidak jalan.

-Skalabilitas  di sistem besar, perlu mekanisme sinkronisasi session antar server (misalnya pakai Redis).

sebuah tip adalah gunakan cookies untuk hal ringan dan non sensitif, sessions untuk data penting yang harus aman
contoh data login dan keranjang bealnja

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tentunya ketika basaha soal sebelumnya tidak aman, cookies adalah standar web tapi ada risikonya, 

beberapa Risiko:
-XSS (Cross-Site Scripting)
Jika attacker berhasil menyisipkan script di halaman, cookie bisa dicuri lewat document.cookie.
berbahaya jika cookie berisi session ID.

-Session Hijacking
Jika session ID dicuri misalnya lewat sniffing di jaringan tidak terenkripsi, attacker bisa mengambil alih sesi user.

-CSRF (Cross-Site Request Forgery)
Karena cookies dikirim otomatis oleh browser pada setiap request ke domain terkait, attacker bisa memanipulasi request jika tidak ada proteksi.

Cara django atasi ancaman tersbeut satu contoh utama melalui settings.py:

- HttpOnly
SESSION_COOKIE_HTTPONLY = True .
Membuat cookie tidak bisa diakses via JavaScript (document.cookie).
Melindungi dari XSS.

- Secure
SESSION_COOKIE_SECURE = True
Cookie hanya dikirim lewat HTTPS, mencegah pencurian via sniffing.

- CSRF Proteksi yang dibahas sebelumnya apada tugas 3
Django otomatis menambahkan token CSRF  pada form.
Mencegah attacker mengirim request palsu menggunakan cookie user.

- Enkripsi/Signing
Django menggunakan cryptographic signing via django.core.signing untuk cookie yang dibuat dengan set_signed_cookie.
Ini memastikan cookie tidak bisa dimodifikasi sembarangan tanpa diketahui server.
 
Cookies tidak sepenuhnya aman secara default, tapi django mengurangi risiko tersebut melalui pengaturan
dan sebagai tambahan developer masih perlu mengaktifkan secure di production agar cookie hanya terkirim via
https

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Secara ringkas:

Jadi pertama saya langsung buat ke modelsnya dulu agar lebih aman, jadi kita harus hubungkan proudct dengan user 
agar kita bisa tau siapa yang milik produk tersebut apakah user a atau user b, jadi untuk lakukannya kita tambahkan
ForeignKey  yang merupakan bawahan dari django db models dan isi parameter tersbut

jangan lupa migrate juga 

kedua buat registrasi login logout views and urls, untuk setiap views tersebut kita pasti perlu buat urls nya.
Untuk kemudahan yang praktis dan juga aman kita gunakan form bawaan django seperti from django.contrib.auth.forms
django.contrib.auth dan packages lainnya. Untuk register view kita gunakan usercreation form dan cek apakah form tersebut valid dari input user dan juga setelah berhasil kita set cookie kepada user tersebut. Hal sama kepada login view tapi kita pakai form.get_user() dan validasi jika login tersebut benar atau tidak dan ada fungsi home
yang mempunyai decorator login_required adalah filter akses jika user valid view dijalankan kalau tidak user di redirectk ke login page

setelah semua itu jangaan lupa tamabahkan url masing-masing dan juga masing-masing tempalte html yang memuat variable yang dynamic dan juga suatu context dari views masing-masing login, regiser dan logout isi context tersebut bisa  dari bawaan django untuk mengatur misal logout time buat masing-masing user yang berbeda. Contoh:

form = UserCreationForm(request.POST)
 context = {'form':form},

 yang merupakan dari library from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

 juga sebagai tambahan views:
 @login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

@login_required adalah filter akses  jika user valid (sudah login), view dijalanka yaitu show product kalau tidak, user di-redirect ke login page pada login html tempalte



