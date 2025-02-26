import paho.mqtt.client as mqtt
import json
import time

broker_address = "test.mosquitto.org"
client = mqtt.Client("TemperatureSensor")
client.connect(broker_address)

device_data = {
    "id": "D1",
    "type": "TemperatureSensor",
    "sensors": [{"id": "S1", "measurement": 23.5}]
}

while True:
    client.publish("sensors/temperature", json.dumps(device_data))
    print("Dados publicados:", device_data)
    time.sleep(5)