# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-22頁
   publish am2320's temperature & humidity to Adafruit IO
"""

import machine
import ubinascii
import time
import am2320
from machine import I2C, Pin
from umqtt.simple import MQTTClient

i2c = I2C(scl=Pin(5), sda=Pin(4))
d = am2320.AM2320(i2c)

config = {
    'broker':'io.adafruit.com',
    'user':'你的帳號',
    'key':'你的AIO KEY',
    'id' : 'room/' + ubinascii.hexlify(machine.unique_id()).decode(),
    'topic_temp' : b'poushen/feeds/temperature',
    'topic_humi' : b'poushen/feeds/humidity'
}

def publish(topic, data):
    client = MQTTClient(client_id=config['id'],
                    server=config['broker'],
                    user=config['user'],
                    password=config['key'])

    client.connect()
    client.publish(topic, data.encode())
    time.sleep(1)
    client.disconnect()
    
def main():
    while True:
        d.measure()
        data = '{}'.format(d.temperature())
        publish(config['topic_temp'], data)
        time.sleep(1)
        data = '{}'.format(d.humidity())
        publish(config['topic_humi'], data)
        time.sleep(8)
        
try:
    main()
except KeyboardInterrupt:
    print('bye')
except Exception as ex:
    print(ex)
