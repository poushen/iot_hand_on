# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-24頁
"""

import machine, time
import ubinascii
import ujson
from umqtt.simple import MQTTClient
from machine import Pin

led = Pin(2, Pin.OUT, value=1)

config = {
    'broker':'io.adafruit.com',
    'user':'你的帳號',
    'key':'你的AIO KEY',
    'id' : 'room/' + ubinascii.hexlify(machine.unique_id()).decode(),
    'topic' : b'poushen/feeds/led'
}

def subCallback(topic, msg):
    #obj = ujson.loads(msg)
    print('led:',  msg.decode())
    print(msg.decode())
    led.value(0) if msg.decode() == 'ON' else led.value(1)

def main():
    client = MQTTClient(client_id=config['id'], 
                        server=config['broker'],
                        user=config['user'],
                        password=config['key'])
    client.set_callback(subCallback)
    client.connect()
    client.subscribe(config['topic'])

    try:
        while True:
            client.check_msg()
            time.sleep(10)
    except Exception as e:
        print(e.args[0])
        client.disconnect()
        print('bye!')
        if e.args[0] == '-1':
            main()