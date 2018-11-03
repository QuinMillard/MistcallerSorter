import serial
import time

class BinController:
    def connect(self):
        self.ser = serial.Serial('/dev/cu.wchusbserial14520', 9600)
        time.sleep(2) # ugly, but required to avoid race condition

    def close(self):
        self.ser.close()

    def place_in_bin_1(self):
        ser.write(b'1')

    def place_in_bin_2(self):
        ser.write(b'2')

    def place_in_bin_3(self):
        ser.write(b'3')

    def place_in_bin_4(self):
        ser.write(b'4')

    def place_in_bin_5(self):
        ser.write(b'5')
