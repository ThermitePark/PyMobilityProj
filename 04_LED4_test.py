from machine import Pin
import time

pins = [2,12,13,22] # My board Pin number
# Please change it according to the board pin number

leds = [Pin(pn, Pin.OUT) for pn in leds ]

try:
    while True:        
        for led_pin in leds:
            led_pin.value(1)
        time.sleep(0.5)
        
        for led_pin in leds:
            led_pin.value(0)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("The program has been terminated.")
    
    for led_pin in leds:
        led_pin.value(0)
        
