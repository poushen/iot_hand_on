# -*- coding: utf-8 -*-

"""
   更新dweet.io以開關LED
"""

from machine import Pin
import time
import urequests as req

sw = Pin(0, Pin.IN)  # D3

def upload_to_dweet(led):
    apiURL = 'http://dweet.io/dweet/for/xxxxabcxxx1234?'
    apiURL += 'led={led}'.format(led=led)
    r = req.get(apiURL)
    print(r.text)
    
def main():
    toggle = True
    while True:
        if sw.value() == 0:
            time.sleep_ms(20)
            if sw.value() == 0:
                while sw.value() == 0:
                    pass
                toggle = not toggle
                if toggle:
                    upload_to_dweet('ON')
                else:
                    upload_to_dweet('OFF')
        time.sleep_ms(50)