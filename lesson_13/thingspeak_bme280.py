# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-22頁
"""

import machine
import ubinascii
import time, gc
import bme280

from machine import Pin, I2C
from umqtt.simple import MQTTClient

i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

config = {
    'broker':'mqtt.thingspeak.com',
    'user':'poushen',
    'key':'VA1MVSS7OPK2HABF',
    'id' : 'room/' + ubinascii.hexlify(machine.unique_id()).decode(),
    'topic' : b'channels/735455/publish/8FDV8A8LXEQ12L3E'
}

def sendData():
    client = MQTTClient(client_id=config['id'],
                    server=config['broker'],
                    user=config['user'],
                    password=config['key'])
    
    temp = bme.read_compensated_data()[0] / 100
    humi = bme.read_compensated_data()[2] / 1024

    data = 'field1={}&field2={}'.format(temp, humi)

    client.connect()
    client.publish(config['topic'], data.encode())
    time.sleep(0.5)
    client.disconnect()
    
    del temp
    del humi
    del data
    del client
    
def main():
    while True:
        sendData()
        gc.collect()
        print('Free RAM after GC:', gc.mem_free())
        time.sleep(18)

try:
    main()
except KeyboardInterrupt:
    print('bye')
except Exception as ex:
    print(ex)