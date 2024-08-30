""" 
Display Gateway 
Module to subscribe mqtt data and display it in a python gui.

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

from tkinter import *
from mqtt_client import MQTTClient
from enterprise import Temperature


class DisplayGateway(MQTTClient):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.topic = f"freezer/+/temperature/celsius"

    def create_window(self):
        # create root window
        self.root = Tk()
        self.root.title("Iot Blog Temperature")
        icon=PhotoImage(file="favicon-32x32.png")
        self.root.iconphoto(True,icon)
        self.root.geometry('350x200')
        self.temperature = StringVar()
        lbl = Label(self.root, textvariable=self.temperature, font=("Helvetica", 32))
        lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.temperature.set("-.- \u00B0C")

    def subscribe(self):
         
        def on_message(client, userdata, msg):
             
            m_decode=str(msg.payload.decode("utf-8","ignore"))
            # print(f"Received {m_decode} from {msg.topic} topic")
            temp = Temperature(m_decode)
            # print(f"Parsed as {temp}  ")
            self.temperature.set(f"{temp.value}.0 \u00B0C")

        self.client.subscribe(self.topic)
        self.client.on_message = on_message
        
    
    def run(self):
        self.connect_mqtt()
        self.client.loop_start()
        self.subscribe()
        self.root.mainloop()

if __name__ == '__main__':
    td = DisplayGateway()
    td.run()
        
        
