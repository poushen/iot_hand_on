# -*- coding: utf-8 -*-

"""
   檢查dweet.io以開關LED
"""
import machine, time
import ujson
from machine import Pin
import urequests as req

led = Pin(2, Pin.OUT, value=1)

def main():
    try:
        while True:
            apiURL = 'http://dweet.io/get/latest/dweet/for/xxxxabcxxx1234'
            r = req.get(apiURL)
            print(r.text)
            obj = ujson.loads(r.text)
            led_status = obj['with'][0]['content']['led']
            print('led: {}'.format(led_status))
            led.value(0) if led_status == 'ON' else led.value(1)
            time.sleep(1)
    except:
        print('Bye')