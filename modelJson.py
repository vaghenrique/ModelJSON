import json

class Device:
    def __init__(self, id, type, sensors):
        self.id = id
        self.type = type
        self.sensors = sensors

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

# Criando um dispositivo baseado no modelo JSON
sensor_data = [{"id": "S1", "measurement": 23.5}]
device = Device("D1", "TemperatureSensor", sensor_data)

# Exibir a estrutura JSON gerada
print(device.to_json())
