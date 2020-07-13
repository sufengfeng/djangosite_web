#!/usr/bin/python3.6  
# -*- coding: utf-8 -*-  
# 循环获取温度，并发布消息
import paho.mqtt.client as mqtt
import json
import threading
from  json_message import MessageType
from json_message import MessageType2dict
import dht11 

from ctypes import *


class Userdata:
    """A simple example class"""
    connected = False
    message_id = 0

    def f(self):
        return 'hello world'


# from w1thermsensor import W1ThermSensor

def get_18b20_temp():
    # sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "00000588806a（自己的设备号，没有‘-’之前的数据）")
    # temperature = sensor.get_temperature()
    temperature = 1
    return temperature


def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp) / 1000
    # Uncomment the next line if you want the temp in Fahrenheit
    # return float(1.8*cpu_temp)+32


from time import sleep


def on_connect(client, userdata, flags, rc):
    userdata.connected = True
    print("Connected with result code: " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_disconnect(client, userdata, msg):
    userdata.connected = False
    print(msg.topic + " " + str(msg.payload))


humidity="0"
temperature="0"
temperature_F="0"
def GetDht11Value():
    global humidity
    global temperature
    global temperature_F
    dht11.Dht11Init()
    while True:
        iret,h,t=dht11.GetDht11Value()
        if iret==0:
            humidity=h
            temperature=t
            temperature_F =float( temperature) * 9. / 5. + 32
            
#             print (humidity)
#             print (temperature)
#             print(temperature_F)
        else:
#             print("")
            pass
        sleep(0.2)

        
userdata = Userdata()
client = mqtt.Client()
client.user_data_set(userdata)


#GetDht11Value()
if __name__ == "__main__":
    global humidity
    global temperature
    global temperature_F
    #create thread for dht11
    threading.Thread(target=GetDht11Value).start()
    while True:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        if client.connect('192.168.1.111', 1883, 600) ==0: # 600为keepalive的时间间隔
            userdata.connected =1
        while userdata.connected:
            userdata.message_id += 1
            message = MessageType('','','','','','')
            message.message_id = userdata.message_id
            message.cpu_temp = get_cpu_temp()
            message.t18b20_temp = get_18b20_temp()
            message.humidity = humidity
            message.temperature = temperature
            message.temperature_F = temperature_F
            json_str = json.dumps(message, default=MessageType2dict)
            client.publish('zjzn/in/jsonbatch', payload=json_str, qos=0)
            sleep(0.5)
        sleep(1)

