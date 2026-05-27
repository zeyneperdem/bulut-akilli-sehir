import time
import json
import random
from awscrt import mqtt
from awsiot import mqtt_connection_builder

ENDPOINT = "a1vsx8dyt3vhc-ats.iot.eu-north-1.amazonaws.com"
PATH_TO_CERT = "355591a7b9a10caf2afa1d1ada5aa65e74ab113e11f48d77c0525b60c4c2d762-certificate.pem.crt"
PATH_TO_KEY = "355591a7b9a10caf2afa1d1ada5aa65e74ab113e11f48d77c0525b60c4c2d762-private.pem.key"
PATH_TO_ROOT = "AmazonRootCA1.pem"

CLIENT_ID = "Akilli_Sehir_Sensoru"
TOPIC = "akillisehir/sensor/veri"

print(f"AWS IoT Core'a bağlanılıyor: {CLIENT_ID}")


mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERT,
    pri_key_filepath=PATH_TO_KEY,
    ca_filepath=PATH_TO_ROOT,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=30
)

connect_future = mqtt_connection.connect()
connect_future.result()
print("Bağlantı Başarılı!")

try:
    while True:
        payload = {
            "cihaz_id": CLIENT_ID,
            "sicaklik": round(random.uniform(15.0, 35.0), 2),
            "hava_kalitesi": random.randint(30, 120),
            "trafik_yogunlugu": random.choice(["Dusuk", "Orta", "Yogun"]),
            "timestamp": int(time.time())
        }
        
        print(f"Gönderilen Veri: {json.dumps(payload)}")
        mqtt_connection.publish(
            topic=TOPIC,
            payload=json.dumps(payload),
            qos=mqtt.QoS.AT_MOST_ONCE
        )
        time.sleep(5)
except KeyboardInterrupt:
    print("\nSimülasyon durduruldu.")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()