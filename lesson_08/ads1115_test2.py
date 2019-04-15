from machine import I2C, Pin
from time import sleep_ms
import ads1x15

addr = 74
gain = 1

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
ads = ads1x15.ADS1115(i2c, addr, gain)

def TempC(voltage):
    degC = ((voltage * 1000) - 500) / 10
    return degC

def main():
    while True:
        voltage = ads.raw_to_v(ads.read(channel1=0)) + 0.01
        print('voltage:{}, Temp C:{}'.format(voltage, TempC(voltage)))
        sleep_ms(1000)

try:
    main()
except:
    print('Bye')
