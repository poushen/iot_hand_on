from machine import I2C, Pin
import ads1x15

addr = 72
gain = 1

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
ads = ads1x15.ADS1115(i2c, addr, gain)

r2 = float(input('R2? '))
vcc = ads.raw_to_v(ads.read(channel1=1))
vout = ads.raw_to_v(ads.read())
I = vout / r2

r1 = r2 * (vcc / vout - 1)

print('R1 = {:.2f} ohm'.format(r1))
print('Vout = {:.2f} V'.format(vout))
print('I = {:.4f} mA'.format(I * 1000))
