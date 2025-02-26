import paho.mqtt.client as mqtt

# Função chamada quando uma mensagem é recebida
def on_message(client, userdata, message):
    print("Mensagem recebida:", str(message.payload.decode("utf-8")))

# Conectar ao broker MQTT
client = mqtt.Client("SensorSubscriber")
client.connect("test.mosquitto.org")

# Assinar o tópico dos sensores
client.subscribe("sensors/temperature")
client.on_message = on_message

# Manter a conexão ativa
client.loop_forever()
