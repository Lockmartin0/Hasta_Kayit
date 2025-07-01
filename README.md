# 🛡️ Şifreli Hasta Kayıt ve Yedekleme Sistemi

Bu proje, Flask tabanlı web uygulamasıyla hasta kayıt yönetimi, kullanıcı giriş/kayıt sistemi ve veritabanı yedekleme işlevlerini barındırır. Uygulama Docker ile konteynerleştirilmiş, MySQL veritabanıyla entegre edilmiştir.


## 🚀 Özellikler

- 👤 Kullanıcı kayıt ve giriş (şifre hashlenmiş şekilde)
- 📋 Hasta bilgilerini ekleme ve listeleme
- 🔍 TC Kimlik Numarası ile hasta arama
- 🧾 `mysqldump` ile manuel veritabanı yedekleme (Flask arayüzünden tetiklenebilir)
- 🐳 Docker ile tam ortam kurulumu

---

## 🗃️ Dosya Yapısı
app.py: Ana Flask uygulamasıdır. Kullanıcı kayıt, giriş, hasta kaydı, arama, backup işlemleri bu dosyada tanımlıdır.

backup_script.py: mysqldump komutunu çalıştırarak veritabanının .sql formatında yedeğini alır. Alınan yedek backups/ klasörüne kaydedilir, işlem durumu backup.log dosyasına yazılır.

Dockerfile: Flask uygulaması için özel imaj oluşturmak amacıyla kullanılır. Python 3.10-slim tabanlı bir ortamda app.py’yi çalıştırmak üzere yapılandırılmıştır.

docker-compose.yml: Flask uygulaması ve MySQL servisini birlikte ayağa kaldırmak için kullanılır. MySQL servisi için ortam değişkenleri, portlar ve volume tanımlamaları yapılır.

requirements.txt: Flask, PyMySQL gibi Python kütüphanelerini içerir. Docker build sırasında bu dosyadaki bağımlılıklar yüklenir.

init.sql: Veritabanının ilk tablolarını (users ve patients) oluşturan SQL komutlarını içerir. MySQL container’ı ayağa kalkarken otomatik olarak çalışır.

templates/: Uygulamanın HTML şablonlarının bulunduğu klasördür.

    backup.html: Veritabanı yedeği alabileceğin sayfa.

    dashboard.html: Hasta kayıt formunun olduğu sayfa.

    login.html: Giriş yapılmasını sağlayan form.

    register.html: Yeni kullanıcı kaydı formu.

    backups/: Yedek dosyalarının (backup_2025-06-28_...sql) saklandığı klasördür.

README.md: Proje hakkında genel bilgileri içeren açıklama dosyasıdır. Kullanım adımları, docker komutları gibi bilgiler burada yer alır.