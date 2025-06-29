# 🛡️ Şifreli Hasta Kayıt ve Yedekleme Sistemi

Bu proje, Flask tabanlı web uygulamasıyla hasta kayıt yönetimi, kullanıcı giriş/kayıt sistemi ve veritabanı yedekleme işlevlerini barındırır. Uygulama Docker ile konteynerleştirilmiş, MySQL veritabanıyla entegre edilmiştir.
Uygulama eğitim amaçlı tasarlanmıştır.

## 🚀 Özellikler

- 👤 Kullanıcı kayıt ve giriş (şifre hashlenmiş şekilde)
- 📋 Hasta bilgilerini ekleme ve listeleme
- 🔍 TC Kimlik Numarası ile hasta arama
- 🔒 IDOR (Insecure Direct Object Reference), SQL Injection, Lfi gibi güvenlik açıklarının gösterimi (bilinçli olarak bırakılmıştır)
- 🧾 `mysqldump` ile manuel veritabanı yedekleme (Flask arayüzünden tetiklenebilir)
- 🐳 Docker ile tam ortam kurulumu
- http://localhost:5000/viewlog?file=backup.log adresini url'de aratarak Lfi zafiyeti gözlemlenebilir. 

---

## 🗃️ Dosya Yapısı

├── Hasta_Kayit-main/
│ ├── app.py # Ana Flask uygulaması
│ ├── backup_script.py # Yedekleme scripti
│ ├── templates/ # HTML şablonları
│    ├── backup.html #Backup alınan sayfa
│    ├── dashboard.html #Hasta kaydı yapılan sayfa
│    ├── login.html #Giriş yapılan sayfa
│    ├── patient.html #IDOR zafiyetli sayfa
│    ├── register.html # Yeni kayıt sayfası
│    ├── search.html #Sql zafiyetli sayfa
│ ├── backups / # Veritabanının backup dosyaları
│ ├──Dockerfile # Web servisi için Dockerfile
│ ├──docker-compose.yml # Tüm sistemi ayağa kaldıran yapı
│ ├──requirements.txt # Python bağımlılıkları
│ ├──init.sql # Mysql database
│ ├──README.md