# Import Module
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
        
        
