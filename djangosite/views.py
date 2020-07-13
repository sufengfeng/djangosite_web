import datetime
import json
import time
from random import random
from re import search

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from djangosite.json_message import dict2MessageType, MessageType2dict

g_messageJson = {'none': 0}
g_message = {}


def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")


def hello(request):
    context = {}
    context['hello'] = 'Hello World!,nihao'
    return render(request, 'hello.html', context)

def form(request):
    context = {}
    return render(request, 'form.html', context)


def index(request):
    return render(request, 'index.html')


def gettemp(request):
    global g_messageJson
    ict0 = json.loads(g_messageJson)
    return JsonResponse(ict0)  # 放字典类型数据

#接收并处理云端订阅的数据
def on_message(client, userdata, msg):
    global g_messageJson
    global g_message
    #    print(msg.topic + " " + str(msg.payload))
    # message = MessageType("", "", "")
    try:
        g_message = json.loads(msg.payload, object_hook=dict2MessageType)
        g_messageJson = msg.payload
    except Exception as err:
        print(err)
        return
    print(g_messageJson.message_id)
