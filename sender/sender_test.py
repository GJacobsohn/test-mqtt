import paho.mqtt.client as mqtt
import paho.mqtt.publish as pub

# BROKER_ADRESS = "test.mosquitto.org"
BROKER_ADDRESS = "192.168.99.100"
TOPIC = "test2"


pub.single(TOPIC, payload="{'message': 'a new message'}".encode(), qos=0, retain=False, hostname=BROKER_ADDRESS, port=1883, client_id="", keepalive=60, will=None, auth={'username':'moovel', 'password':'123'}, tls=None, protocol=mqtt.MQTTv31)
# manual interface
# client_sender.publish(TOPIC, "{'message': 'a new message'}".encode())

