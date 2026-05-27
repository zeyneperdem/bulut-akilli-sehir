import json
import boto3

# DynamoDB Kaynak Bağlantısı
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('akilli_sehir_verileri')

def lambda_handler(event, context):
    print(f"Gelen Ham Veri: {json.dumps(event)}")
    
    try:
        # Veri Tiplerinin DynamoDB Tablo Şemasına Göre Dönüştürülmesi
        cihaz_id = str(event['cihaz_id'])
        timestamp = str(event['timestamp'])  # Sıralama Anahtarı (Sort Key) ile Uyumlandırma
        sicaklik = str(event['sicaklik'])
        hava_kalitesi = int(event['hava_kalitesi'])
        trafik_yogunlugu = str(event['trafik_yogunlugu'])
        
        # DynamoDB Tablosuna Item Ekleme
        table.put_item(
            Item={
                'cihaz_id': cihaz_id,
                'timestamp': timestamp,
                'sicaklik': sicaklik,
                'hava_kalitesi': hava_kalitesi,
                'trafik_yogunlugu': trafik_yogunlugu
            }
        )
        print("BAŞARILI: Veri dönüştürülerek DynamoDB'ye yazıldı!")
        
    except Exception as e:
        print(f"Veritabanına yazma aşamasında hata oluştu: {str(e)}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('İşlem Başarıyla Tamamlandı')
    }
