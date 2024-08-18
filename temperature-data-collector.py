import random
import time
from paho.mqtt import client as mqtt_client
from enterprise import TagPayload

import uuid

class TemperatureDataCollector:

    def __init__(self):
        self.broker = '127.0.0.1'
        self.port = 1883
        self.topic = f"freezer/{str(uuid.uuid4())}/temperature/celsius"
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.client = None
        self.temperature = random.randint(-10, 30)

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

    def get_temperature(self):
        delta = random.randint(-4, 4)
        temperature = temperature + delta
        if temperature < -10 :
            temperature = -10
        if temperature > 30:
            temperature = 30
        return temperature
        
        

    def publish(self):
         
        temperature = random.randint(-10, 30)
        while True:
            time.sleep(60)
             
            msg = TagPayload(self.get_temperature()).get_json_string()
            result = self.client.publish(self.topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{self.topic}`")
            else:
                print(f"Failed to send message to topic {self.topic}")
            time.sleep(60)
 

    def run(self):
        self.connect_mqtt()
        self.client.loop_start()
        self.publish()
        self.client.loop_stop()


if __name__ == '__main__':
    tdc = TemperatureDataCollector()
    tdc.run()

    
