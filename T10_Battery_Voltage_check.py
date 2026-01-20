from  machine import ADC
import time

battery = ADC(26)

try:
    while True:
        value = battery.read_u16()
        voltage = value / 65535 * 3.4
        voltage *= 3.08
        print(value, voltage)
        time.sleep(0.2)
    
    
    
    
except KeyboardInterrupt:
     print("The program has been terminated.")