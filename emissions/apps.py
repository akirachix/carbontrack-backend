import threading
import time
import paho.mqtt.client as mqtt
import requests  
import json

import os
from dotenv import load_dotenv
load_dotenv(override=True)

BROKER = os.getenv('BROKER')
PORT = int(os.getenv('PORT')) 
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
TOPIC = os.getenv('TOPIC')
API_URL = os.getenv('API_URL')


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        client.subscribe(TOPIC, qos=1) 
        print("Connected successfully to the broker")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        payload_str = msg.payload.decode("utf-8", errors="ignore").strip()
        data = json.loads(payload_str)
        
        if isinstance(data, dict):
            def safe_get(key):
                val = data.get(key)
                return val if val is not None else "N/A"
                        
            api_payload = {
                "device_id": safe_get('device_id'),
                "emission_rate": safe_get('co2_emission_kgs') if safe_get('co2_emission_kgs') != "N/A" else 0.0
            }

            response = requests.post(API_URL, json=api_payload)
            if response.status_code == 201:
                print("Emission data successfully sent to API")
            else:
                print(f"Failed to send data to API: {response.status_code} - {response.text}")

        else:
            print(data)
    except json.JSONDecodeError:
        print(f"\nRaw message received on topic {msg.topic}: {payload_str}")
    except Exception as e:
        print(f"\nError decoding message on topic {msg.topic}: {e}")

class MqttThread(threading.Thread):
    def run(self):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set(USERNAME, PASSWORD)
        client.connect(BROKER, PORT, keepalive=120)
        client.loop_start()  
        while True:
            time.sleep(1)

from django.apps import AppConfig  

class EmissionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emissions"

    def ready(self):
        mqtt_thread = MqttThread()
        mqtt_thread.daemon = True
        mqtt_thread.start()