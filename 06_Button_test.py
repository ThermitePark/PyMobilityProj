from machine import Pin
import time
# Number 4, 5 => My board Pin Number
left = Pin(5,Pin.IN)
right = Pin(4,Pin.IN)
# .value() => Current Value
try:
    while True:
        leftinput = left.value()
        rightinput = right.value()
        print(f'left button : {leftinput}, right button : {rightinput}')
        time.sleep(0.01)

except KeyboardInterrupt:
    print("The program has been terminated.")