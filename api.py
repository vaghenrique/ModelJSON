from flask import Flask, jsonify, request

app = Flask(__name__)

devices = [
    {
        "id": "D1",
        "type": "TemperatureSensor",
        "sensors": [
            {"id": "S1", "measurement": 23.5}
        ]
    },
    {
        "id": "D2",
        "type": "HumiditySensor",
        "sensors": [
            {"id": "H1", "measurement": 60.2}
        ]
    }
]

@app.route("/devices", methods=["GET"])
def get_devices():
    return jsonify(devices)

@app.route("/devices/<device_id>", methods=["GET"])
def get_device(device_id):
    device = next((d for d in devices if d["id"] == device_id), None)
    return jsonify(device) if device else (jsonify({"error": "Device not found"}), 404)

@app.route("/devices", methods=["POST"])
def add_device():
    new_device = request.json
    devices.append(new_device)
    return jsonify(new_device), 201

if __name__ == "__main__":
    app.run(debug=True)