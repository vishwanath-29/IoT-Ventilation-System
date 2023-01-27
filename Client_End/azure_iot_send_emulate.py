import random  
#import adafruit_dht
import time
#import board

from azure.iot.device import IoTHubDeviceClient, Message  
# dhtDevice = adafruit_dht.DHT11(board.D3,use_pulseio=False)

CONNECTION_STRING = "HostName=Iot-Ventilation-System.azure-devices.net;DeviceId=Raspberry-pi-3;SharedAccessKey=fAG59knKTbgIZmd1ydlhoV6Z1KsDsTKs5rrF/0d42AQ="  

MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}'  

while True:
    
    def iothub_client_init():
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
        return client  
    def iothub_client_telemetry_sample_run():  
        try:  
            client = iothub_client_init()  
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
            while True: 
                try:
                    temperature=random.randint(30,45)
                    humidity=random.randint(40,85)
                    #temperature = dhtDevice.temperature
                    #humidity = dhtDevice.humidity 
                except RuntimeError:
                    print("Error")
                msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity)  
                message = Message(msg_txt_formatted)  
                print( "Sending message: {}".format(message) )  
                client.send_message(message)  
                print ( "Message successfully sent" )  
                time.sleep(3)  
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" ) 
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        iothub_client_telemetry_sample_run()
