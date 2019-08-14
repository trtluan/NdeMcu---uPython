'''

This file is executed on every boot (including wake-boot from deepsleep)
#import esp

#esp.osdebug(None)

import gc

import os

#import webrepl

#webrepl.start()

gc.collect()

'''

Complete project details at https://RandomNerdTutorials.com
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'vine.vide.vince'
password = '00000'
mqtt_server = '00.000.000.00'

#EXAMPLE IP ADDRESS
#mqtt_server = '000.168.0.000'
client_id = 'zerynth-mqtt'# ubinascii.hexlify(machine.unique_id())
topic_sub = b'temp/random'
topic_pub = b'hello'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

print('tentando conectar')
while station.isconnected() == False:
pass

print('Connection successful')
print(station.ifconfig())
