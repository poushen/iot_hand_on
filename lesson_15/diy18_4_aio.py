# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-24頁
"""

import machine, time, gc
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
    value = msg.decode()
    print('led:',  value)
    led.value(0) if value.upper() == 'ON' else led.value(1)

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
            time.sleep(2)
    except KeyboardInterrupt:
        print('bye')
    except OSError as ex:
        print(ex.args[0])
        if ex.args[0] == -1:
            print('woooops')
            gc.collect()
            time.sleep(1)
            main()
        # ---
    finally:
        client.disconnect()
