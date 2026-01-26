from machine import UART, Pin
import time

uart1 = UART(0,9600,bits = 8, parity = None, stop =1, tx = Pin(16), rx = Pin(17))

try:
    while True:
        if uart1.any() > 0:
            rxData = uart1.read()
            print(rxData, rxData.decode())
            
except KeyboardInterrupt:
    print("The program has been terminated.")