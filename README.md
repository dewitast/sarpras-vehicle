# sarpras  

## Petunjuk Instalasi Pertama Kali  
1. Unduh XAMPP di https://www.apachefriends.org/download.html dan install XAMPP di komputer Anda.  
2. Unduh Anaconda di https://www.continuum.io/downloads dan install Anaconda di komputer Anda.  
3. Buka XAMPP Control Panel dan klik Start pada Module MySQL. Klik tombol Shell untuk membuka command line MySQL
4. Login dengan akun MySQL Anda:
`$ mysql -u root -p`
5. Setelah berhasil login, buat database kosong baru dengan nama `sarpras3`:
`create database sarpras3;`
6. Extract file 'sarpras3.zip' pada komputer Anda.
7. Buka file `sarpras/sarpras/settings.py` dengan text editor (misalnya Notepad) dan ubah setting database (USER dan PASSWORD dengan username dan password MySQL pada komputer Anda).
8. Buka command prompt pada folder yang berhasil di-extract.
9. Setting environment dengan memasukkan perintah berikut.
`$ conda env create -f environment.yml`  
`$ activate django`  
10. Buat akun baru dengan memasukkan perintah di bawah ini. Isi username, alamat email, dan password yang diinginkan.
`$ python manage.py createsuperuser`
11. Lakukan migrasi database dengan memasukkan perintah berikut. 
`$ python manage.py migrate`  
`$ python manage.py loaddata data_supir_dan_kendaraan.json`  
12. Jalankan aplikasi dengan memasukkan perintah berikut.
`$ python manage.py runserver`  
13. Buka web browser (misalnya Google Chrome) dan buka alamat `http://localhost:8000` pada browser.  


## Prepare Database  
1. Create empty database named: sarpras3  
2. Clone this project  
3. Change database setting (USER and PASSWORD) in `sarpras/sarpras/settings.py` with your local computer's settings  

## Installation with Anaconda  

Install Anaconda: https://www.continuum.io/downloads  

Create environment:  
`$ conda env create -f environment.yml`  

Activate environment:  
`$ activate django`  

Run script:  
`$ python manage.py migrate`  
`$ python manage.py runserver`  

Open browser:  
http://127.0.0.1:8000/  

Deactivate environment:  
`$ deactivate`  

## Create Django admin user
Source: https://docs.djangoproject.com/en/1.10/intro/tutorial02/#creating-an-admin-user  

1. Run script:  
`$ python manage.py createsuperuser`  
2. Fill the prompt.  
3. Run script:  
`$ python manage.py runserver`  
4. Open http://127.0.0.1:8000/admin/  