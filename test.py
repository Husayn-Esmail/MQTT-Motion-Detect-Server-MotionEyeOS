import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.publish("homebridge/motion", "reset")
client.subscribe("homebridge/motion")
client.on_message
client.disconnect()

def on_message(client, userdata, message):
    print('received message' + message.topic + ' ' + str(message.payload))
