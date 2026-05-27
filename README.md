# bulut-akilli-sehir
# AWS IoT ve Bulut Bilişim ile Akıllı Şehir Entegrasyonu Projesi

Bu proje, modern akıllı şehir mimarilerinde çevresel verilerin (sıcaklık, hava kalitesi, trafik yoğunluğu vb.) IoT cihazları tarafından simüle edilerek bulut ortamına aktarılması, sunucusuz (serverless) mimarilerle işlenerek NoSQL veritabanında depolanması ve iş zekası araçlarıyla gerçek zamanlı analitik panellere dönüştürülmesini içerir.

Sistem Mimarisi ve Veri Akışı

Proje mimarisi tamamen bulut yerli (cloud-native) ve altyapı yönetim maliyetini sıfıra indiren sunucusuz (serverless) yapılardan oluşmaktadır.

Edge / Cihaz Katmanı:Python 3 (MQTT protokolü ile güvenli veri üretimi)
Veri Alımı (Ingestion): AWS IoT Core (X.509 Sertifika Güvenlikli)
Veri İşleme (Compute): AWS Lambda (Python 3 tabanlı veri tipi dönüştürme ve ETL)
Veri Depolama (NoSQL): Amazon DynamoDB (Anahtar-Değer veri modeli)
İş Zekası & Görselleştirme: Amazon QuickSight (BI Analitik Paneli)


Kullanılan Teknolojiler

Diller & Protokoller: Python 3, MQTT, JSON
AWS Servisleri: AWS IoT Core, AWS Lambda, Amazon DynamoDB, Amazon QuickSight, AWS IAM (Kimlik ve Erişim Yönetimi)
Python Kütüphaneleri `paho-mqtt`, `boto3`, `json`, `time`, `random`



Proje Dosyaları

`sensor1.py`: Yerel bilgisayarda çalışan, akıllı şehir sensör verilerini üreterek AWS IoT Core'a şifreli (TLS/SSL) gönderen simülatör kodu.
`lambda_function.py`: IoT Core Kural Motoru (Rule Engine) tarafından tetiklenen, gelen ham verileri DynamoDB şemasına uygun biçimde dönüştüren ve veritabanına kaydeden AWS Lambda kaynak kodu.


 Kurulum ve Çalıştırma

1. Yerel Cihaz Simülatörünün Başlatılması
Gerekli MQTT kütüphanesini indirin:
'''bash
pip install paho-mqtt

2. AWS Lambda Konfigürasyonu
Lambda fonksiyonuna AmazonDynamoDBFullAccess IAM politikası atanmıştır.

timestamp verisinin veritabanı sıralama anahtarı (Sort Key) ile uyuşması için str() tip dönüşümü fonksiyon içinde dinamik olarak yapılmaktadır.

3. Amazon DynamoDB Tablo Yapısı
Tablo Adı: akilli_sehir_verileri

Partition Key (Bölüm Anahtarı): cihaz_id (String)

Sort Key (Sıralama Anahtarı): timestamp (String)

Proje Çıktıları ve Doğrulama (Testler)
DynamoDB Veri Doğrulama: Simülatörden akan verilerin DynamoDB konsolunda Scan ve Query işlemleriyle sıfır hata payıyla depolandığı doğrulanmıştır.

Amazon QuickSight Analitik Çıktıları: * Sıcaklık ve Hava Kalitesi Karma Grafiği: Zaman serisi boyunca sıcaklık ve hava kalitesi indeksleri yığılmış dikey sütunlar halinde incelenmiştir.

Hava Kalitesi Zaman Serisi: Şehir genelindeki hava kalitesi trendleri kronolojik olarak sütun grafiklerine dönüştürülmüştür.
