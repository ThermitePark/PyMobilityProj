from machine import Pin
import time

led_pin = Pin(25,Pin.OUT)
# 10% Average Brightness
try:
    while True:
        led_pin.value(1)
        time.sleep(0.001) # 1 : 9
        led_pin.value(0)
        time.sleep(0.009) # 9 : 1
except KeyboardInterrupt:
    print("The program has been terminated.")