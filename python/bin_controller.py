import serial
import time

class BinController:
    def connect(self):
        print("[INFO] Opening serial connection.")
        #self.ser = serial.Serial('/dev/cu.wchusbserial14520', 9600)
        #time.sleep(2) # ugly, but required to avoid race condition

    def close(self):
        print("[INFO] Closing serial connection.")
        #self.ser.close()

    def place_in_bin(self, bin_number):
        switcher = {
            1: self.place_in_bin_1,
            2: self.place_in_bin_2,
            3: self.place_in_bin_3,
            4: self.place_in_bin_4,
            5: self.place_in_bin_5,
        }
        switcher.get(bin_number, "Invalid method")()

    ## -----------------------------------------------

    def place_in_bin_1(self):
        #self.ser.write(b'1')
        return None

    def place_in_bin_2(self):
        #self.ser.write(b'2')
        return None

    def place_in_bin_3(self):
        #self.ser.write(b'3')
        return None

    def place_in_bin_4(self):
        #self.ser.write(b'4')
        return None

    def place_in_bin_5(self):
        #self.ser.write(b'5')
        return None
