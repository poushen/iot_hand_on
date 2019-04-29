from machine import Pin
from dht import DHT22
from time import sleep

d = DHT22(Pin(2))

while True:
    d.measure()
    print('Temp: {}{}C, Humi: {} %'.format(d.temperature(), '\u00b0', d.humidity()))
    sleep(4)
    