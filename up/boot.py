import urequests
import os
import time
import network

def connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("aa", "12345678")
    time.sleep_ms(500)
    print(sta_if.isconnected())

def doIt():
    response = urequests.get('https://raw.githubusercontent.com/TheNameIsSamSamuelson/esp32/master/main/start.py')
    file = open("/main.py", 'w')
    os.listdir()
    file.write(response.text)
    file.close()
    os.remove("/boot.py")
    os.rename('./main.py','./boot.py')
    os.listdir()

def all():
    connect()
    doIt()

    #Comment to make it different
from scron.week import simple_cron
simple_cron.run() # You have to run it once. This initiates the SimpleCRON action, and reserve one timmer.
simple_cron.add('Every second minute',lambda *a,**k: all(),minutes=range(0, 59, 2),seconds=0)