# KX022 SPI test code
import kx022_spi as kx022
import time
from machine import Pin, SPI

cs = Pin(16, Pin.OUT)   # D0
# Hardware SPI
# D5 GPIO14 SCK
# D6 GPIO12 MISO
# D7 GPIO13 MOSI
spi = SPI(1, baudrate=1000000, polarity=0, phase=0)

kx = kx022.KX022(spi, cs)

id = kx.oneByteRead(kx022.KX_WHO_AM_I)
print('Device ID:{}'.format(id))

kx.setOpMode(kx022.KX_PC1_STANDBY)
kx.setPerfMode(kx022.KX_RES_LOW)     # 8bit resolution
kx.setGRange(kx022.KX_GSEL_2G)       # g range: +-2G
kx.setODR(kx022.KX022_50HZ)
kx.setOpMode(kx022.KX_PC1_OPERATE)

readings = [0,0,0]
rate = 1 / 64  # unit: g

while True:
    kx.getOutput(readings)
    x = readings[0] * rate
    y = readings[1] * rate
    z = readings[2] * rate
    print('x={:.2f}, \t\t y={:.2f}, \t\t z={:.2f}'.format(x,y,z))
    time.sleep_ms(50)
