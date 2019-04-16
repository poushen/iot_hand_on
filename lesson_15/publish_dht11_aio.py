# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-22頁
   publish dht11's temperature & humidity to Adafruit IO
"""

import machine
import ubinascii
import time
import dht
from machine import Pin
from umqtt.simple import MQTTClient

d = dht.DHT11(Pin(2))

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
    print(ex.args[0])
