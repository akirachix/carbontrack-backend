import os
import ssl
import json
import requests
import paho.mqtt.client as mqtt

# Load config vars from Heroku
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT", 8883))
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOPIC = os.getenv("TOPIC")
API_URL = os.getenv("API_URL")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to HiveMQ Cloud")
        client.subscribe(TOPIC)
        print(f"📡 Subscribed to {TOPIC}")
    else:
        print(f"❌ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"📥 Received on {msg.topic}: {payload}")
    try:
        # Forward MQTT payload to your API
        response = requests.post(API_URL, json={
            "topic": msg.topic,
            "payload": payload
        })
        print(f"➡️ API Response {response.status_code}: {response.text}")
    except Exception as e:
        print("❌ Failed to send to API:", e)

def main():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)

    # TLS is required by HiveMQ Cloud
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()