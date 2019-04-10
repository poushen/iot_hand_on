from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led(0)
    sleep(1)
    led(1)
    sleep(1)
