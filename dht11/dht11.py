# -*- coding: utf-8 -*-
from ctypes import *
from time import *
library = cdll.LoadLibrary("./libdht11.so")
#   library.pointerTest.argtypes = [POINTER(c_int), POINTER(c_float), c_char_p]
library.GetDht11Value.argtypes = [ c_char_p, c_char_p]
library.GetDht11Value.restype = c_int

library.Dht11Init.restype = c_int
#引入动态库libDemo.so
def  GetDht11Value():
    global library
    humidity = (c_char*32)()
    temperature = (c_char*32)()
    #library.GetDht11Value(humidity, byref(b), word)
    iret=library.GetDht11Value(humidity, temperature)
    return iret,humidity.value,temperature.value


def Dht11Init():
    global library
    ret=library.Dht11Init()
    return ret

if __name__=="__main__":
    Dht11Init()
    while True:
        iret,humidity,temperature=GetDht11Value()
        if iret==0:
            print (humidity)
            print (temperature)
            F =float( temperature) * 9. / 5. + 32
            print(F)
            print("")
        else:
#           print("")
            pass
        sleep(0.2)
