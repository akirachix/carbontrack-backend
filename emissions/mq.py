import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs="path/to/isrgrootx1.pem", tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set("CarbonTrack", "@Carbontrack2025")
client.connect("57652ef3c2f34337b4fe5619db6f16b9.s1.eu.hivemq.cloud", 8883)
client.loop_start()