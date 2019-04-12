from machine import Pin, SPI

ADXL345_BW_RATE_REG = const(0x2C)
ADXL345_POWER_CTL_REG = const(0x2D)
ADXL345_DATA_FORMAT_REG = const(0x31)
ADXL345_DATAX0_REG = const(0x32)
ADXL345_DATAX1_REG = const(0x33)
ADXL345_DATAY0_REG = const(0x34)
ADXL345_DATAY1_REG = const(0x35)
ADXL345_DATAZ0_REG = const(0x36)
ADXL345_DATAZ1_REG = const(0x37)

ADXL345_3200HZ = const(0x0F)
ADXL345_1600HZ = const(0x0E)
ADXL345_800HZ  = const(0x0D)
ADXL345_400HZ  = const(0x0C)
ADXL345_200HZ  = const(0x0B)
ADXL345_100HZ  = const(0x0A)
ADXL345_50HZ   = const(0x09)
ADXL345_25HZ   = const(0x08)
ADXL345_12HZ5  = const(0x07)
ADXL345_6HZ25  = const(0x06)

ADXL345_SPI_READ   = const(0x80)
ADXL345_SPI_WRITE  = const(0x00)
ADXL345_MULTI_BYTE = const(0x40)

class ADXL345:
    #cs = Pin(15, Pin.OUT)
    #spi = SPI(1, baudrate=1000000, polarity=1, phase=1)

    def __init__(self, spi, cs):
        self.__spi = spi
        self.__cs = cs
        self.setPowerControl(0x00)          # standby mode
        self.setDataFormatControl(0x0B)     # Full resolution, +/-16g, 4mg/LSB
        self.setDataRate(ADXL345_400HZ)
        self.setPowerControl(0x08)          # mesaurement mode
    
    def setPowerControl(self, setting):
        self.oneByteWrite(ADXL345_POWER_CTL_REG, setting)
    
    def setDataFormatControl(self, setting):
        self.oneByteWrite(ADXL345_DATA_FORMAT_REG, setting)
    
    def setDataRate(self, rate):
        # Get the current register contents, so we don't clobber the power bit.
        registerContents = self.oneByteRead(ADXL345_BW_RATE_REG)
        
        registerContents &= 0x10
        registerContents |= rate
        
        self.oneByteWrite(ADXL345_BW_RATE_REG, registerContents)
    
    def getOutput(self, readings):
        buffer = [0,0,0,0,0,0]
        self.multiByteRead(ADXL345_DATAX0_REG, buffer, 6)
        readings[0] = (int(buffer[1]) << 8) | buffer[0]
        readings[1] = (int(buffer[3]) << 8) | buffer[2]
        readings[2] = (int(buffer[5]) << 8) | buffer[4]
        readings[0] = readings[0] - 65536 if readings[0] > 32767 else readings[0]
        readings[1] = readings[1] - 65536 if readings[1] > 32767 else readings[1]
        readings[2] = readings[2] - 65536 if readings[2] > 32767 else readings[2]
        
    def oneByteWrite(self, address, data):
        tx = (ADXL345_SPI_WRITE | (address & 0x3F))
        self.__cs.value(0)
        self.__spi.write(bytes([tx, data]))
        self.__cs.value(1)
    
    def oneByteRead(self, address):
        tx = (ADXL345_SPI_READ | (address & 0x3F))
        rx = 0
        self.__cs.value(0)
        self.__spi.write(bytes([tx]))
        rx = self.__spi.read(1)[0]
        self.__cs.value(1)
        return rx
    
    def multiByteRead(self, startAddress, buff, size):
        tx = (ADXL345_SPI_READ | ADXL345_MULTI_BYTE | (startAddress & 0x3F))
        self.__cs.value(0)
        self.__spi.write(bytes([tx]))
        for i in range(size):
            buff[i] = self.__spi.read(1)[0]
        self.__cs.value(1)