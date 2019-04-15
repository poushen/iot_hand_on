from machine import Pin, ADC
import time

adc = ADC(0)

while True:
    val = adc.read()
    x = (val - 512) / 1024 * 3.3 / 0.3
    print('x = {:0.3f}g'.format(x))
    time.sleep(0.1)