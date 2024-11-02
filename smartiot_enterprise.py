"""
Enterprise helps
A collection of helper classes

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

import uuid
from enterprise import TagPayload

class TagMqtt():
    def __init__(self, publish_topic, subscription_topic):
        self.subscription_topic = subscription_topic
        self.publish_topic = publish_topic
        self.payload = "{}"

    def publish(self, mqtt_client):
        mqtt_client.publish(self.publish_topic, self.payload)

    def subscribe(self, mqtt_client):
        mqtt_client.subscribe(self.subscription_topic)

    def add_callback(self, mqtt_client, the_callback):
        mqtt_client.message_callback_add(self.subscription_topic, the_callback)
    

class TagMqttValue(TagMqtt):
    def __init__(self, publish_topic, subscription_topic):
        super().__init__(publish_topic, subscription_topic)
        self.payload = TagPayload()

    def update_payload(self, json_value):
        self.payload = None
        self.payload = TagPayload(json_value)

class MqttRequest(TagMqtt):
    def __init__(self, publish_topic, subscription_topic):
        super().__init__(f"{publish_topic}.request", f"{subscription_topic}.request")
        self.payload = "{}"


class MqttResponse(TagMqtt):
    def __init__(self, publish_topic, subscription_topic, tag_value):
       super().__init__(f"{publish_topic}.response", f"{subscription_topic}.response")
       self.tag_value = tag_value

             
class Tag():

    def __init__(self, publish_topic, subscription_topic):
        self.snapshot = TagMqttValue(publish_topic, subscription_topic)
        self.request = MqttRequest(publish_topic, subscription_topic)
        self.response = MqttResponse(publish_topic, subscription_topic, self.snapshot)
        
class TemperatureDataPoint(Tag):
    def __init__(self):
        publish_topic = f"freezer/{str(uuid.uuid4())}/{self.__class__.__name__.lower()}"
        subscription_topic = f"freezer/+/{self.__class__.__name__.lower()}"
        super().__init__(publish_topic, subscription_topic)
        
