from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT)
for i in range(3):
    led(0)
    sleep_ms(200)
    led(1)
    sleep_ms(200)
    
