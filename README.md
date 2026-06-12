# TB200B Readout
Python code using [serial interface](https://www.pyserial.com/) to take measurements with EC Sense [TB200B](https://ecsense.com/ec-sense-products/?filters=product_cat[165]) based gas sensors.

This is an independent implementation of the communication protocol of the TB200B (EC Sense). It is not affiliated with, endorsed, or supported by EC Sense. All reference documents, datasheets, and specifications belong to their respective copyright holders.
## Installation
First clone the repository:
```
git clone https://github.com/MaxLKP/tb200b.git
```
Then install the package:
```
pip install ./tba200b
```
## Use
All functionality is adopted from the EC Sense communication protocol. 
```
import tba200b
hf_sensor = tba200b.TBA200B("COM3")
```
### Get Sensor Parameters
```
TBA200B.get_sensorparameters() -> dict
```
Returns a dict with the sensor parameters in the form
```
{"type": sensor, "maxrange": maximum_range, "unit": unit, "sign": sign, "decimals": decimals}
```
### Get Combined Reading of Concentration, Temperature and Pressure
```
TBA200B.get_combinedread() -> dict
```
Returns a dict with the measurements taken in the form
```
{"conc_mgm3": conc_mgm3, "conc_ppm": conc_ppm, "temp": temp, "hum": hum}
```
### Get Concentration Measurement only
```
TBA200B.get_concentration -> dict
```
Returns a dict containing the measured concentration
```
{"conc_mgm3": conc_mgm3, "conc_ppm": conc_ppm}
```
If the checksum for a given response of the sensor fails, all values in the dict returned by a given function will be set to ```-1.```.

### License
This is an independent implementation of the communication protocol of the TB200B (EC Sense). It is not affiliated with, endorsed, or supported by EC Sense. All reference documents, datasheets, and specifications belong to their respective copyright holders.

[MIT License](https://github.com/MaxLKP/tb200b/blob/main/LICENSE)
