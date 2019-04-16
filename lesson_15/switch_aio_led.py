# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-22頁
"""

import machine
import ubinascii
import time
from machine import Pin
from umqtt.simple import MQTTClient

sw = Pin(0, Pin.IN)  # D3
toggle = True

config = {
    'broker':'io.adafruit.com',
    'user':'你的帳號',
    'key':'你的AIO KEY',
    'id' : 'room/' + ubinascii.hexlify(machine.unique_id()).decode(),
    'topic' : b'poushen/feeds/led'
}

def publish(data):
    client = MQTTClient(client_id=config['id'],
                    server=config['broker'],
                    user=config['user'],
                    password=config['key'])

    client.connect()
    client.publish(config['topic'], data.encode())
    time.sleep(1)
    client.disconnect()
    
def main():
    global toggle
    while True:
        if sw.value() == 0:
            time.sleep_ms(20)
            if sw.value() == 0:
                while sw.value == 0:
                    pass
                toggle = not toggle
                if toggle:
                    publish('ON')
                else:
                    publish('OFF')
        time.sleep_ms(50)

try:
    main()
except KeyboardInterrupt:
    print('bye')
except Exception as ex:
    print(ex.args[0])
    print('bye bye')
