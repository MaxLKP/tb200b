import serial as serial
import time
from tb200b.header import *

# Project:
# https://github.com/MaxLKP/tb200b

class TB200B:
    def __init__(self, port) -> None:
        self.port = port
        #self.serial = serial.Serial(port, baudrate = BAUDRATE, parity = PARITY, bytesize = BYTESIZE, stopbits = STOPBITS, rtscts = RTSCTS, timeout = TIMEOUT)
        self.commands = COMMANDS
    
    def __write_command(self, command: bytes) -> None:
        self.serial.write(command)
        time.sleep(0.1)
    
    def __read_response(self):
        response = self.serial.readlines()
        time.sleep(0.1)
        return response

    def set_activemode(self) -> None:
        self.__write_command(self.commands["command_1"])
    
    def set_passivemode(self) -> None:
        self.__write_command(self.commands["command_2"])
    
    def get_sensorparameters(self, answer) -> dict:
        #self.__write_command(self.commands["command_3"])
        #response = self.__read_response()
        response = answer
        sensor = SENSOR_TYPES_INVERSE[response[0]]
        maximum_range = (response[1] << 8) | response[2]
        unit = UNITS_INVERSE[response[3]]
        decimals = (response[7]) >> 4
        sign = response[7] & 0b00001111
        if sign == 0:
            sign = 1
        elif sign == 1:
            sign = -1
        sensor_info = {"type": sensor, "maxrange": maximum_range, "unit": unit, "sign": sign, "decimals": decimals}
        return sensor_info

    def get_combinedread(self, answer) -> dict:
        #self.__write_command(self.commands["command_5"])
        #response = self.__read_response()
        response = answer
        conc_mgm3 = float(response[2]) * 256 + float(response[3])
        conc_ppm = float(response[6]) * 256 + float(response[7])
        temp = float((response[8] << 8) | response[9]) / 100
        hum = float((response[10] << 8) | response[11]) / 100
        combined = {"conc": conc_mgm3, "temp": temp, "hum": hum}
        print(conc_mgm3, conc_ppm)
        return combined

tb200b = TB200B("COM2")
#print(tb200b.get_sensorparameters(b'\x18\x00\xc8\x02\x00\x00\x00\x01\x35'))
#print(tb200b.get_combinedread(b'\xFF\x87\x00\x2a\x03\xE8\x00\x20\x09\xc4\x13\x88\xdc'))
tb200b.get_combinedread(b'\xff\x87\x05\x88\x00\n\x06\xd5\x08\xa2\x0f9\x15')
#print(units_inverse[0x08])
#print(dict((v, k) for k, v in units.items()))