# TB200B Readout
Python code using [serial interface](https://www.pyserial.com/) to take measurements with EC Sense [TB200B](https://ecsense.com/ec-sense-products/?filters=product_cat[165]) based gas sensors.
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
hf_sensor = tba200b.TBA200b("COM3")
```
### License
[MIT License](https://github.com/MaxLKP/tb200b/blob/main/LICENSE)
