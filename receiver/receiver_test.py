import paho.mqtt.client as mqtt

# BROKER_ADRESS = "test.mosquitto.org"
BROKER_ADDRESS = "192.168.99.100"
TOPIC = "test2"

# The callback for when the receiver receives a CONNACK response from the sender.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code %s" % rc)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # receiver.subscribe("$SYS/#")
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the sender.
def on_message(client, userdata, msg):
    print("received: %s %s" % (msg.topic,msg.payload))

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: %s %s" % (mid,granted_qos))


client_receiver = mqtt.Client()
client_receiver.username_pw_set("moovel", "123")

client_receiver.on_connect = on_connect
client_receiver.on_message = on_message
client_receiver.on_subscribe = on_subscribe
client_receiver.connect(BROKER_ADDRESS, 1883, 60)

client_receiver.connect(BROKER_ADDRESS, 1883, 60)
client_receiver.subscribe(TOPIC)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client_receiver.loop_forever()

