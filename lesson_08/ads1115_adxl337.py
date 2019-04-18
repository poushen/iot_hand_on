from machine import I2C, Pin
from time import sleep_ms
import ads1x15

addr = 72
gain = 1

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
ads = ads1x15.ADS1115(i2c, addr, gain)
    
def GValue(voltage):
    g = (voltage - 1.65) * 1000 / 330
    return g

def main():
    while True:
        vx = ads.raw_to_v(ads.read(channel1=0))
        vy = ads.raw_to_v(ads.read(channel1=1))
        vz = ads.raw_to_v(ads.read(channel1=2))
        print('x:{:.4f}g \t y:{:.4f}g \t z:{:.4f}g'.format(GValue(vx), GValue(vy), GValue(vz)))
        sleep_ms(100)

try:
    main()
except Exception as ex:
    print(ex)
    print('Bye')