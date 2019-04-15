from machine import Pin, I2C

class TMP102:
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
    #slave_address = 0x48
    
    def __init__(self, slave_address=0x48):
        self.__slave_address = slave_address

    def get_TempC(self, data):
        val = int.from_bytes(data, 'big', False) >> 4
        if val > 0x7FF:
            val = val | 0xF000
        return val * 0.0625

    def get_register_data(self, register):
        data = None
        while data is None:
            TMP102.i2c.writeto(self.__slave_address, bytes([register]))
            data = TMP102.i2c.readfrom(self.__slave_address, 2)
        return data
    
    def readTempC(self):
        data = self.get_register_data(0)
        return self.get_TempC(data)
    
    def wakeup(self):
        data = self.get_register_data(1)
        data1 = data[0]
        data1 &= 0xFE      # set bit0 = 0
        TMP102.i2c.writeto_mem(self.__slave_address, 1, bytes([data1]))

    def sleep(self):
        data = self.get_register_data(1)
        data1 = data[0]
        data1 |= 0x01     # set bit0 = 1
        TMP102.i2c.writeto_mem(self.__slave_address, 1, bytes([data1]))

    def set_alert_polarity(self, active_low):
        data = self.get_register_data(1)
        data1 = data[0]
        if active_low:
            data1 &= 0xFB  # set bit2 = 0
        else:
            data1 |= 0x04  # set bit2 = 1

        TMP102.i2c.writeto_mem(self.__slave_address, 1, bytes([data1]))
        
    def set_one_shot(self):
        data = self.get_register_data(1)
        data1 = data[0]
        data1 |= 0x80     # set bit7 = 1
        TMP102.i2c.writeto_mem(self.__slave_address, 1, bytes([data1]))

    def get_one_shot(self):
        while True:
            data = self.get_register_data(1)
            data1 = data[0]
            data1 = (data1 >> 7) & 0x01
            if data1 != 0:
                break
        return self.get_register_data(0)

    def one_shot_read_TempC(self):
        self.set_one_shot()
        return self.get_TempC(self.get_one_shot())
