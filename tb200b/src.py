import serial as serial
import time
from tb200b.header import *

# Project:
# https://github.com/MaxLKP/tb200b

class TB200B:
    def __init__(self, port):
        self.port = port
        self.serial = serial.Serial(port, baudrate = BAUDRATE, parity = PARITY, bytesize = BYTESIZE, stopbits = STOPBITS, rtscts = RTSCTS, timeout = TIMEOUT)
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
    
    def get_sensorparameters(self) -> dict:
        self.__write_command(self.commands["command_3"])
        response = self.__read_response()
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

    def get_combinedread(self) -> dict:
        self.__write_command(self.commands["command_5"])
        response = self.__read_response()
        conc = float(response[2]) * 256 + float(response[3])
        temp = float((response[8] << 8) | response[9]) / 100
        hum = float((response[10] << 8) | response[11]) / 100
        combined = {"conc": conc, "temp": temp, "hum": hum}
        return combined
