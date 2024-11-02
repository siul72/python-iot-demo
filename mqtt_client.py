"""
MQTTClient
A wrapper class to paho-mqtt client with some additional functionality

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

import random
import time
from paho.mqtt import client as mqtt_client
 

class MQTTClient:

    def __init__(self, broker="127.0.0.1", port=1883):
        self.broker = broker
        self.port = port
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.client = None
        

    def connect_mqtt(self, connect_callback = None, disconnect_callback = None):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
                self.client.publish("test", "test")
            else:
                print("Failed to connect, return code %d\n", rc)
                

        def on_disconnect(client, userdata, flags, rc):
            if rc == 0:
                print("Disconnected to MQTT Broker!")
            else:
                print("Error on disconnect, return code %d\n", rc)
                
        self.client = mqtt_client.Client(self.client_id)
        # client.username_pw_set(username, password)
        self.client.on_connect = on_connect
        if connect_callback:
            self.client.on_connect = connect_callback

        self.client.on_disconnect = on_disconnect
        if disconnect_callback:
            self.client.on_disconnect = disconnect_callback
        print(f"connect to {self.broker}:{self.port}-->")
        self.client.connect_async(self.broker, self.port)
        print(f"current client {self.client}")

if __name__ == '__main__':
    print("start")
    tdc = MQTTClient()
    tdc.connect_mqtt()
    tdc.client.loop_start()
    
 
 

    
