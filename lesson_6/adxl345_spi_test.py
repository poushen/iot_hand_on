# ADXL345 SPI test code
import adxl345_spi
import time
from machine import Pin, SPI

cs = Pin(15, Pin.OUT)
spi = SPI(1, baudrate=1000000, polarity=1, phase=1)

adx = adxl345_spi.ADXL345(spi, cs)
readings = [0,0,0]
rate = 32000 / 8192

while True:
    adx.getOutput(readings)
    x = readings[0] * rate
    y = readings[1] * rate
    z = readings[2] * rate
    print('x={:.2f}, \t\t y={:.2f}, \t\t z={:.2f}'.format(x,y,z))
    time.sleep_ms(50)
