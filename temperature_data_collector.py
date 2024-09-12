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
        
    def publish(self):
         
        while self.connected:
            self.temperature.snapshot.payload.update_value(self.update_temperature())
            msg = self.temperature.snapshot.payload.get_json_string()
            result = self.client.publish(self.temperature.snapshot.publish_topic, msg)
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{self.temperature.snapshot.publish_topic}`")
            else:
                print(f"Failed to send message to topic {self.temperature.snapshot.publish_topic}")
            time.sleep(60)

    def on_connect(self, client, userdata, flags, rc):
        print("mqtt connected!")
        self.connected = True 
        self.publish()
         
    def on_disconnect(self, userdata, flags, rc):
        print("mqtt disconnected!")
        self.connected = False 

    def run(self):
        self.connect_mqtt(self.on_connect, self.on_disconnect)
        self.client.loop_start()
   


if __name__ == '__main__':
    tdc = TemperatureDataCollector()
    tdc.run()

    

