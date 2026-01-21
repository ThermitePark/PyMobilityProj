from machine import Pin
import time

P1,P2 = Pin(1,Pin.OUT),Pin(0,Pin.OUT)

#Depending on the board, the motor code’s 1 and 0 may be reversed,
#so if it behaves unexpectedly, please double-check the settings.


#Rotate
P1.value(1)
P2.value(0)
time.sleep(2)


#Stop
P1.value(0)
P2.value(0)
time.sleep(2)


#Rotate
P1.value(0)
P2.value(1)
time.sleep(2)


#Stop
P1.value(0)
P2.value(0)

