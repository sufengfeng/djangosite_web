from time import sleep

import paho.mqtt.client as mqtt
import json
from djangosite.json_message import dict2MessageType
from djangosite.json_message import MessageType
from djangosite.views import on_message


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))





def on_disconnect(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def deamon_mqtt_subcript():
    while True:
        # 接受
        client = mqtt.Client()
        client.on_connect = on_connect

        client.on_message = on_message
        client.on_disconnect = on_disconnect
        client.connect('127.0.0.1', 1883, 600)  # 600为keepalive的时间间隔
        client.subscribe('zjzn/in/jsonbatch', qos=0)
        client.loop_forever()  # 保持连接
        print("subscribe zjzn/in/jsonbash again!!!")
        sleep(1)
