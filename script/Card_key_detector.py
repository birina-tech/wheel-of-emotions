import machine
from pn532 import PN532_I2C

i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5))
nfc = PN532_I2C(i2c, debug=False)
nfc.SAM_configuration()

print("Scanning... Tap your keys one by one.")

while True:
    uid = nfc.read_passive_target(timeout=500)
    if uid is not None:
        print("UID Found:", '.'.join(['%02X' % x for x in uid]))
