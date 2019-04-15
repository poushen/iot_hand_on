from machine import Pin, I2C
from servo import Servo
import time, math

PCF8591 = 0x48
CH0 = b'\x00'
CH1 = b'\x01'

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
s = Servo(0)
s.rotate(0)

while True:
    r = i2c.writeto(PCF8591, CH0)
    data0 = i2c.readfrom(PCF8591, 1)
    data0 = i2c.readfrom(PCF8591, 1)
    
    r = i2c.writeto(PCF8591, CH1)
    data1 = i2c.readfrom(PCF8591, 1)
    data1 = i2c.readfrom(PCF8591, 1)
    
    #print('CH0:{:03}, CH1:{:03}, CH2:{:03}, CH3:{:03}'.format(data0[0], data1[0]))
    
    # calculate g value
    x = (data0[0] - 128) / 256 * 3.3 / 0.3
    y = (data1[0] - 128) / 256 * 3.3 / 0.3
    r = math.atan2(x, y)
    d = r * 180 / 3.14159
    
    if d >= 0:
        s.rotate(int(d))
    
    print('r = {} \t\t d = {}'.format(r, d))
    
    time.sleep_ms(100)
