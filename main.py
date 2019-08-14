# NdeMcu---uPython
sensor de gas

"""Implements a HD44780 character LCD connected via NodeMCU GPIO pins."""

from machine import Pin, ADC
from utime import sleep, ticks_ms
from nodemcu_gpio_lcd import GpioLcd
from umqttsimple import MQTTClient


        


#test_main()



# Complete project details at https://RandomNerdTutorials.com

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()
  
  


# Wiring used for this example:
#
#  1 - Vss (aka Ground) - Connect to one of the ground pins on you NodeMCU board.
#  2 - VDD - Connect to 3V
#  3 - VE (Contrast voltage) - I'll discuss this below
#  4 - RS (Register Select) connect to D0 (as per call to GpioLcd)
#  5 - RW (Read/Write) - connect to ground
#  6 - EN (Enable) connect to D1 (as per call to GpioLcd)
#  7 - D0 - leave unconnected
#  8 - D1 - leave unconnected
#  9 - D2 - leave unconnected
# 10 - D3 - leave unconnected
# 11 - D4 - connect to D2 (as per call to GpioLcd)
# 12 - D5 - connect to D3 (as per call to GpioLcd)
# 13 - D6 - connect to D4 (as per call to GpioLcd)
# 14 - D7 - connect to D5 (as per call to GpioLcd)
# 15 - A (BackLight Anode) - Connect to 3V
# 16 - K (Backlight Cathode) - Connect to Ground
#
# On 14-pin LCDs, there is no backlight, so pins 15 & 16 don't exist.
#
# The Contrast line (pin 3) typically connects to the center tap of a
# 10K potentiometer, and the other 2 legs of the 10K potentiometer are
# connected to pins 1 and 2 (Ground and VDD)


def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    AdcPin=machine.ADC(0)
    '''lcd = GpioLcd(rs_pin=Pin(16),
                  enable_pin=Pin(5),
                  d4_pin=Pin(4),
                  d5_pin=Pin(0),
                  d6_pin=Pin(2),
                  d7_pin=Pin(14),
                  num_lines=2, num_columns=16)'''
    lcd = GpioLcd(rs_pin=Pin(0),
                  enable_pin=Pin(2),
                  d4_pin=Pin(14),
                  d5_pin=Pin(12),
                  d6_pin=Pin(13),
                  d7_pin=Pin(15),
                  num_lines=2, num_columns=16)                  
    lcd.putstr("It Works!\nSecond Line")
    sleep(3)
    lcd.clear()
    count = 0
    lcd.putstr("Iot Impacta 2019") 
    
    try:
      print('Tendando acessar Mosquitto')
      client = connect_and_subscribe()
      client.check_msg()
      print('Mosquitto acessado')
    except OSError as e:
      restart_and_reconnect()   
      
    while True:
        lcd.move_to(0, 1)
        msg = str((AdcPin.read()-10)*36.5/96)
        lcd.putstr('Tep. = {}'.format(msg))
        #lcd.putstr("%7d" % (ticks_ms() // 1000))
        try:
           print('lendo servidor')
           print(client.check_msg())
           print('servidor lido')
           print('Publicando', msg)
           client.publish('temp/random', msg)
           print('Publicado')
        except OSError as e:
           restart_and_reconnect()        
        sleep(1)



test_main()
