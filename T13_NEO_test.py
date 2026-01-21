from machine import Pin
from neopixel import NeoPixel
import time
#PIN => Board NeoPixel Number
PIN =3
count = 36
# count => the number of NeoPixels
pin = Pin(PIN, Pin.OUT)
neo = NeoPixel(pin, count)
# Five times
for i in range(5):
    
    np.fill((0,0,128))
    np.write()
    time.sleep(1)
    
    np.fill((0,0,0))
        np.write()
        time.sleep(1)
    
    
