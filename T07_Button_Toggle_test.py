from machine import Pin
import time
button = Pin(5,Pin.IN)
led = Pin(13,Pin.OUT)

led_on = False
prev = 0

try:
    #curr => Current Button Value
    curr = button.value()
    # The moment the button is pressed => value = 1
    if curr == 1 and prev == 0:
        led_on = not led_on
        led.value(led_on)    
    
    prev = curr
    time.sleep(0.02)
    
except KeyboardInterrupt:
    print("The program has been terminated.")
