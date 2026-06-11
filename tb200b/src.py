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
    
    def __read_response(self, response_length: int):
        response = self.serial.read(response_length)
        time.sleep(0.1)
        return response

    def set_activemode(self) -> None:
        self.__write_command(self.commands["command_1"])
    
    def set_passivemode(self) -> None:
        self.__write_command(self.commands["command_2"])
    
    def get_sensorparameters(self) -> dict:
        self.__write_command(self.commands["command_3"])
        response = self.__read_response(9)
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
        self.__write_command(self.commands["command_6"])
        response = self.__read_response(13)
        conc_mgm3 = float(response[2]) * 256 + float(response[3])
        conc_ppm = float(response[6]) * 256 + float(response[7])
        temp = float((response[8] << 8) | response[9]) / 100
        hum = float((response[10] << 8) | response[11]) / 100
        combined = {"conc_mgm3": conc_mgm3, "conc_ppm": conc_ppm, "temp": temp, "hum": hum}
        return combined
        
    def get_concentration(self) -> dict:
        self.__write_command(self.commands["command_5"])
        response = self.__read_response(9)
        parameters = self.get_sensorparameters()
        decimals = parameters["decimals"]
        conc_mgm3 = (response[2] * 256 + response[3]) / 10**decimals
        conc_ppm = (response[6] * 256 + response[7]) / 10**decimals
        concentration = {"conc_mgm3": conc_mgm3, "conc_ppm": conc_ppm}
        return concentration