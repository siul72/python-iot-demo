""" 
Temperature Data Collector
Module to collect data and published to a mqtt broker.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Luis Coelho"
__contact__ = "luis.coelho.720813@gmail.com"
__date__ = "2024.08"
__deprecated__ = False
__license__ = "BSD 2-Clause License"
__status__ = "Production"
__version__ = "0.0.1"

from mqtt_client import MQTTClient 
import uuid
import random
import time
from smartiot_enterprise import TemperatureDataPoint
 

class TemperatureDataCollector(MQTTClient):

    def __init__(self):
        super().__init__()
        self.temperature = TemperatureDataPoint()
        self._source_data = random.randint(-10, 30)
        
        
    def update_temperature(self):
        delta = random.randint(-4, 4)
        _data = self._source_data + delta
        if _data < -10 :
            _data = -10
        if _data > 30:
            _data = 30
        self._source_data = _data    
        return self._source_data

    
    
    def subscribe(self):

        def on_request_message(client, userdata, msg):
            # check if the request is valid
            print(f"request to update")
            self.publish()

        self.temperature.request.subscribe(self.client)
        self.temperature.request.add_callback(self.client, on_request_message)
        
        
    def publish(self):
             
        self.temperature.snapshot.payload.update_value(self.update_temperature())
        msg = self.temperature.snapshot.payload.get_json_string()
        result = self.client.publish(self.temperature.snapshot.publish_topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{self.temperature.snapshot.publish_topic}`")
        else:
            print(f"Failed to send message to topic {self.temperature.snapshot.publish_topic}")
            

    def on_connect(self, client, userdata, flags, rc):
        print("mqtt connected!")
        self.connected = True
        self.subscribe()
        self.publish()
         
    def on_disconnect(self, userdata, flags, rc):
        print("mqtt disconnected!")
        self.connected = False 

    def run(self):
        self.connect_mqtt(self.on_connect, self.on_disconnect)
        self.client.loop_start()
        run = True
        while run:
            time.sleep(10)
            run = self.connected
            if not run:
                break
            self.publish()
            self.client.loop(timeout=1.0, max_packets=1)
   


if __name__ == '__main__':
    print("start")
    tdc = TemperatureDataCollector()
    tdc.run()

    

