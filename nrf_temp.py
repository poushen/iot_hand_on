from board import LED
from machine import RTCounter, Temp
from ubluepy import Service, Characteristic, UUID, Peripheral, constants


def event_handler(id, handle, data):
    global rtc
    global periph
    global serv_env_sense
    global notif_enabled

    if id == constants.EVT_GAP_CONNECTED:
        # indicated 'connected'
        LED(1).on()

    elif id == constants.EVT_GAP_DISCONNECTED:
        # stop low power timer
        rtc.stop()
        # indicate 'disconnected'
        LED(1).off()
        # restart advertisment
        periph.advertise(device_name="micr_temp", services=[serv_env_sense])

    elif id == constants.EVT_GATTS_WRITE:
        # write to this Characteristic is to CCCD
        if int(data[0]) == 1:
            notif_enabled = True
            # start low power timer
            rtc.start()
        else:
            notif_enabled = False
            # stop low power timer
            rtc.stop()


def send_temp(timer_id):
    global notif_enabled
    global char_temp

    if notif_enabled:
        # measure chip temperature
        temp = Temp.read()
        temp = temp * 100
        char_temp.write(bytearray([temp & 0xFF, temp >> 8]))


# start off with LED(1) off
LED(1).off()

# use RTC1 as RTC0 is used by bluetooth stack
# set up RTC callback every 5 second
rtc = RTCounter(1, period=50, mode=RTCounter.PERIODIC, callback=send_temp)

notif_enabled = False

uuid_env_sense = UUID("0x181A")  # Environmental Sensing service
uuid_temp = UUID("0x2A6E")  # Temperature characteristic

serv_env_sense = Service(uuid_env_sense)

temp_props = Characteristic.PROP_NOTIFY | Characteristic.PROP_READ
temp_attrs = Characteristic.ATTR_CCCD
char_temp = Characteristic(uuid_temp, props=temp_props, attrs=temp_attrs)

serv_env_sense.addCharacteristic(char_temp)

periph = Peripheral()
periph.addService(serv_env_sense)
periph.setConnectionHandler(event_handler)
periph.advertise(device_name="micr_temp", services=[serv_env_sense])