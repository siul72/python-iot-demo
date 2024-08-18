from mqtt_client import MQTTClient 
from enterprise import TagPayload
import uuid
import random
import time

class TemperatureDataCollector(MQTTClient):

    def __init__(self):
        super().__init__() 
        self.topic = f"freezer/{str(uuid.uuid4())}/temperature/celsius"
        self.temperature = random.randint(-10, 30)

    def update_temperature(self):
        delta = random.randint(-4, 4)
        self.temperature = self.temperature + delta
        if self.temperature < -10 :
            self.temperature = -10
        if self.temperature > 30:
            self.temperature = 30
        return self.temperature
        
    def publish(self):
         
        while True:
            
            self.update_temperature() 
            msg = TagPayload(self.temperature).get_json_string()
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

    
