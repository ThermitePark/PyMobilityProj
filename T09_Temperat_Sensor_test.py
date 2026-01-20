import time
import machine
# .ADC(4) => Channel Number 4
sensor = machine.ADC(4)
conversion = 3.3/65535
# 3.3 => Voltage, 65535 => Maximum of Unsigned 16bit

try:
    while True:
        inp = sensor.read_u16()
        senConvers = inp * conversion
        
        temperat = 27 - (senConvers - 0.707) / 0.0018
        print(temperat)
        time.sleep(1)

except KeyboardInterrupt:
     print("The program has been terminated.")