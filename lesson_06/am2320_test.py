import time
import am2320
from machine import I2C, Pin
i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = am2320.AM2320(i2c)

while True:
    sensor.measure()
    print('Temp: {}{}C, Humi: {} %'.format(sensor.temperature(), '\u00b0', sensor.humidity()))
    #print('Temp: {}C, Humi: {} %'.format(sensor.temperature(), sensor.humidity()))
    time.sleep(4)
    