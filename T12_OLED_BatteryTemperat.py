from machine import ADC
from M02_OLED_Class_Module import OLED

OLED.begin()
battery = ADC(26)
temperat = ADC(4)
conversion = 3.3 / 65535

try:
    while True:
        batvalue = battery.read_u16()
        batvoltage = batvalue / 65535 * 3.3
        batvoltage *= 3.08
        
        tempin = temperat.read_u16()
        tempconvers = tempin * conversion
        temperature = 27 - (tempconvers - 0.7) / 0.0017
        
        OLED.oled_print(f'BAT: {batvoltage:.1f}V, Temp: {temperature}')
        time.sleep(2)
    
    
    
    
    
except KeyboardInterrupt:
    print("The program has been terminated.")