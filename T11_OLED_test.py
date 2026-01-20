from M01_OLED_SSD1306_Module import SSD1306_I2C
from machine import Pin, I2C

i2c = I@C(0,scl = Pin(21), sda = Pin(20), freq = 200000)
display = SSD1306_I2C(128,32,i2c)

display.text('Hi, OLED Test 1,2,3')
display.show()