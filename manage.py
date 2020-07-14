#!/usr/bin/env python
import copy
import json
import os
import sys
import time

import django
import threading
from django.core.management import execute_from_command_line

# 更新噪声数据后台线程
from djangosite.json_message import MessageType
from djangosite.views import g_message


def deamon_process():
    while True:
        # 接受
        global g_message
        msg = MessageType(g_message.message_id, g_message.t18b20_temp, 53, 53, 45, 65)

        msg.message_id = msg.message_id + 1
        msg.t18b20_temp = msg.t18b20_temp + 0.1
        #    print(msg.topic + " " + str(msg.payload))
        # message = MessageType("", "", "")
        try:
            g_message = copy.deepcopy(msg)
        except Exception as err:
            print(err)
            return
        print(g_message.message_id)

        time.sleep(1)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")

    threading.Thread(target=deamon_process, daemon=True).start()
    execute_from_command_line(sys.argv)
