#from machine import Pin, SPI

# Registers.
KX_CNTL1 = const(0x18)
KX_ODCNTL = const(0x1B)
KX_XOUT_L = const(0x06)
KX_XOUT_H = const(0x07)
KX_YOUT_L = const(0x08)
KX_YOUT_H = const(0x09)
KX_ZOUT_L = const(0x0A)
KX_ZOUT_H = const(0x0B)
KX_WHO_AM_I = const(0x0F)

# Data Rate
KX022_100HZ = const(0x03)
KX022_50HZ = const(0x02)
KX022_25HZ = const(0x01)
KX022_12HZ = const(0x00)  # 12.5Hz
KX022_6HZ = const(0x0B)   # 6.25Hz

# Operation Mode
KX_PC1_STANDBY = const(0x00)
KX_PC1_OPERATE = const(0x01)

# Performance Mode
KX_RES_LOW = const(0x00)
KX_RES_HIGH = const(0x01)

# G-range
KX_GSEL_2G = const(0x00)
KX_GSEL_4G = const(0x01)
KX_GSEL_8G = const(0x02)

class KX022:
    
    def __init__(self, spi, cs):
        self.__spi = spi
        self.__cs = cs
        
    # operation mode: standby 0x00, operate 0x01
    def setOpMode(self, mode):
        reg = self.oneByteRead(KX_CNTL1)
        reg &= 0x7F
        reg |= mode << 7
        self.oneByteWrite(KX_CNTL1, reg)
        
    # resolution: low 0x00, high 0x01
    def setPerfMode(self, mode):
        reg = self.oneByteRead(KX_CNTL1)
        reg &= 0xBF
        reg |= mode << 6;
        self.oneByteWrite(KX_CNTL1, reg)
        
    # g-range: 2g 0x00, 4g 0x01, 8g 0x02
    def setGRange(self, mode):
        reg = self.oneByteRead(KX_CNTL1)
        reg &= 0xE7
        reg |= mode << 3
        self.oneByteWrite(KX_CNTL1, reg)
        
    # output data rate
    def setODR(self, rate):
        reg = self.oneByteRead(KX_ODCNTL)
        reg &= 0xF0
        reg |= rate
        self.oneByteWrite(KX_ODCNTL, reg)
        
    def getOutput(self, readings):
        buffer = [0,0,0,0,0,0]
        self.multiByteRead(KX_XOUT_L, buffer, 6)
        readings[0] = buffer[1]
        readings[1] = buffer[3]
        readings[2] = buffer[5]
        readings[0] = readings[0] - 256 if readings[0] > 127 else readings[0]
        readings[1] = readings[1] - 256 if readings[1] > 127 else readings[1]
        readings[2] = readings[2] - 256 if readings[2] > 127 else readings[2]
        
    def oneByteWrite(self, address, data):
        tx = address & 0x7F;                     # set for write, msb=0 for write
        self.__cs.value(0)
        self.__spi.write(bytes([tx, data]))
        self.__cs.value(1)
        
    def oneByteRead(self, address):
        tx = address | 0x80;                     # set for Read, msb=1 for read
        rx = 0
        self.__cs.value(0)
        self.__spi.write(bytes([tx]))
        rx = self.__spi.read(1)[0]
        self.__cs.value(1)
        return rx
    
    def multiByteRead(self, startAddress, buff, size):
        tx = startAddress | 0x80;   # set for Read, multiple bytes operation
        self.__cs.value(0)
        self.__spi.write(bytes([tx]))
        for i in range(size):
            buff[i] = self.__spi.read(1)[0]
        self.__cs.value(1)