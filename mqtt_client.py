import random
from paho.mqtt import client as mqtt_client
 

class MQTTClient:

    def __init__(self, broker="127.0.0.1", port=1883):
        self.broker = broker
        self.port = port
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.client = None
        

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.client = mqtt_client.Client(self.client_id)
        # client.username_pw_set(username, password)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
 
 

    
