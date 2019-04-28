from machine import I2C, Pin
import ads1x15
import ssd1306
import time

addr = 72
gain = 1

sw = Pin(14, Pin.IN, Pin.PULL_UP) # D5

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
ads = ads1x15.ADS1115(i2c, addr, gain)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def measure(r2):
    vcc = ads.raw_to_v(ads.read(channel1=1))
    vout = ads.raw_to_v(ads.read())
    I = vout / r2
    r1 = r2 * (vcc / vout - 1)
    
    print('---------')
    print('R1 = {:.2f} ohm'.format(r1))
    print('Vcc = {:.2f} V'.format(vcc))
    print('Vout = {:.2f} V'.format(vout))
    print('I = {:.4f} mA'.format(I * 1000))
    
    oled.fill(0)
    oled.text('ohms', 0, 0)
    oled.text('R1 = {:.2f}'.format(r1), 10, 30)
    oled.show()
    
r2 = 9990
while True:
    if sw.value() == 0:
        time.sleep_ms(20)
        if sw.value() == 0:
            while sw.value() == 0:
                pass
            measure(r2)