from machine import Pin
import time

led_pin = Pin(25,Pin.OUT)
# 0.5s + 0.5s => 1s => 1Hz LED Control
try:
    while True:
        led_pin.value(1)
        time.sleep(0.5)
        led_pin.value(0)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("The program has been terminated.")