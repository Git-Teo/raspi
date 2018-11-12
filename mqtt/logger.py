import paho.mqtt.client as mqtt

f = open("log.txt", "w")

def onMessage(client, userdata, message):
    f.write(str(message.payload.decode("utf-8"))

client = mqtt.Client()
client.on_message= onMessage
client.connect("localhost")
client.loop_start()
client.subscribe("sensors")
client.loop_stop()
