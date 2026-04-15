commands = {
    "command_1": bytes([0xFF, 0x01, 0x78, 0x40, 0x00, 0x00, 0x00, 0x00, 0x47]), # Set Active Upload
    "command_2": bytes([0xFF, 0x01, 0x78, 0x41, 0x00, 0x00, 0x00, 0x00, 0x46]), # Set Passive Upload
    "command_3": bytes([0xD1]), # Sensor Type, Maximum Range, Unit, Decimal Places
    "command_4": bytes([0xD7]), # Sensor Type, Maximum Range, Unit, Decimal Places
    "command_5": bytes([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]), # Gas Concentration
    "command_6": bytes([0xFF, 0x01, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0x78]), # Combined Reading
}

sensor_types = { "HCHO": 0x17, "VOC": 0x18, "CO": 0x19, "Cl2": 0x1A, "H2": 0x1B, "H2S": 0x1C, "HCl": 0x1D, "HCN": 0x1E, "HF": 0x1F, "NH3": 0x20, "NO2": 0x21, "O2": 0x22, "O3": 0x23, "SO2": 0x24, "HBr": 0x25, "Br2": 0x26, "F2": 0x27, "PH3": 0x28, "AsH3": 0x29, "SiH4": 0x2A, "GeH4": 0x2B, "B2H6": 0x2C, "BF3": 0x2D, "WF6": 0x2E, "SiF4": 0x2F, "XeF2": 0x30, "TiF4": 0x31, "SMELL": 0x32, "IAQ": 0x33, "AQI": 0x34, "NMHC": 0x35, "SOx": 0x36, "NOx": 0x37, "NO": 0x38, "C4H8": 0x39, "C3H6O2": 0x3A, "CH4S": 0x3B, "C5H8": 0x3C, "C4H10": 0x3D, "C2H6": 0x3E, "C8H14": 0x3F, "C3H3N": 0x41, "C2H7N": 0x42, "C2H6O": 0x43, "CS2": 0x44, "C2H6S": 0x45, "C2H6S2": 0x46, "C2H4": 0x47, "CH3OH": 0x48, "C3H10": 0x49, "C3H6": 0x4A, "C3H8": 0x4B, "CH3COOH": 0x4C, "ClO2": 0x4D, "H2O2": 0x4E, "N2H4": 0x4F, "C2H8N2": 0x50, "C2HCl3": 0x51, "CHCl3": 0x52, "C2H2Cl4": 0x53, "H2Se": 0x54, "Other": 0x55}
sensor_types_inverse = {23: 'HCHO', 24: 'VOC', 25: 'CO', 26: 'Cl2', 27: 'H2', 28: 'H2S', 29: 'HCl', 30: 'HCN', 31: 'HF', 32: 'NH3', 33: 'NO2', 34: 'O2', 35: 'O3', 36: 'SO2', 37: 'HBr', 38: 'Br2', 39: 'F2', 40: 'PH3', 41: 'AsH3', 42: 'SiH4', 43: 'GeH4', 44: 'B2H6', 45: 'BF3', 46: 'WF6', 47: 'SiF4', 48: 'XeF2', 49: 'TiF4', 50: 'SMELL', 51: 'IAQ', 52: 'AQI', 53: 'NMHC', 54: 'SOx', 55: 'NOx', 56: 'NO', 57: 'C4H8', 58: 'C3H6O2', 59: 'CH4S', 60: 'C5H8', 61: 'C4H10', 62: 'C2H6', 63: 'C8H14', 65: 'C3H3N', 66: 'C2H7N', 67: 'C2H6O', 68: 'CS2', 69: 'C2H6S', 70: 'C2H6S2', 71: 'C2H4', 72: 'CH3OH', 73: 'C3H10', 74: 'C3H6', 75: 'C3H8', 76: 'CH3COOH', 77: 'ClO2', 78: 'H2O2', 79: 'N2H4', 80: 'C2H8N2', 81: 'C2HCl3', 82: 'CHCl3', 83: 'C2H2Cl4', 84: 'H2Se', 85: 'Other'}

units = {"mg/m3 and ppm": 0x02, "ppb and ug/m3": 0x04, r"% and 10g/m3": 0x08}
units_inverse = {2: 'mg/m3 and ppm', 4: 'ppb and ug/m3', 8: '% and 10g/m3'}