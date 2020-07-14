import datetime
import json
from django.shortcuts import render
from django.http import  JsonResponse
from djangosite.json_message import MessageType2dict, MessageType

# Create your views here.

g_message = MessageType(1,0,0,0,0,0)

def index(request):
    return render(request, 'index.html')


def gettemp(request):
    global g_message
    ict0 = json.dumps(g_message, default=MessageType2dict)
    message_json=eval(ict0)
    return JsonResponse(message_json)  # 放字典类型数据


