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
    'broker':'mqtt.thingspeak.com',
    'user':'poushen',
    'key':'你的MQTT API Key',
    'id' :'iot/'+ubinascii.hexlify(machine.unique_id()).decode(),
    'topic': b'channels/頻道ID/subscribe/json/你的讀取API KEY'

def subCallback(topic, msg):
    obj = ujson.loads(msg)
    print('led:',  obj['field1'])
    led.value(0) if obj['field1'] == 'ON' else led.value(1)

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
    except:
        client.disconnect()
        print('bye!')