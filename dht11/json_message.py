import json


class MessageType:
    def __init__(self,message_id ,t18b20_temp ,cpu_temp,humidity,temperature,temperature_F):
        self.message_id =message_id
        self.t18b20_temp =t18b20_temp
        self.cpu_temp =cpu_temp
        self.humidity=humidity
        self.temperature=temperature
        self.temperature_F=temperature_F



def MessageType2dict(msg):
    return {
        'message_id': msg.message_id,
        't18b20_temp': msg.t18b20_temp,
        'cpu_temp': msg.cpu_temp,
        'humidity':msg.humidity,
        'temperature':msg.temperature,
        'temperature_F':msg.temperature_F
    }
def dict2MessageType(d):
    return MessageType(d['message_id'], d['t18b20_temp'], d['cpu_temp'],d['humidity'], d['temperature'], d['temperature_F'])


if __name__ == "__main__":
    s = MessageType("132","2","3","4","5","6")
    json_str=json.dumps(s, default=MessageType2dict)
    print(json_str)
    message=json.loads(json_str, object_hook=dict2MessageType)
    print(message.message_id)

