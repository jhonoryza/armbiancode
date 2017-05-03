import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("jardik.web.id",1883,60)
client.loop_forever()
