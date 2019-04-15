# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-22頁
"""

import machine
import ubinascii
import time
from machine import Pin
from umqtt.simple import MQTTClient

config = {
    'broker':'io.adafruit.com',
    'user':'你的帳號',
    'key':'你的AIO KEY',
    'id' : 'room/' + ubinascii.hexlify(machine.unique_id()).decode(),
    'topic' : b'poushen/feeds/led'
}

client = MQTTClient(client_id=config['id'],
                    server=config['broker'],
                    user=config['user'],
                    password=config['key'])

data = 'ON'

client.connect()
client.publish(config['topic'], data.encode())
time.sleep(2)
client.disconnect()
