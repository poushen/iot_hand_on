from machine import Pin
from time import sleep_ms

led = Pin(14, Pin.OUT) # D5
for i in range(10):
	led(1)
	sleep_ms(500)
	led(0)
	sleep_ms(500)
