import paho.mqtt.client as mqtt
import json

f = open("log.txt", "w")
ldrf = open("ldrlog.txt", "w")

def onMessage(client, userdata, message):
    f.write(str(message.payload.decode("utf-8"))
    msg = json.encode(str(message.payload.decode("utf-8")))
    if msg["lidarreadings"]:
        ldrf.write(msg["lidarreadings"])
	
client = mqtt.Client()
client.on_message= onMessage
client.connect("localhost")
client.loop_start()
client.subscribe("sensors")
client.loop_stop()
