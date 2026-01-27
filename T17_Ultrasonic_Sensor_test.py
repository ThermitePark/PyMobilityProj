from machine import Pin, time_pulse_us
import time

SOUND_SPEED = 340
TRIG_PULSE_DURATION_US = 10

trigPin = Pin(15,Pin.OUT)
echoPin = Pin(14,Pin.IN)

try:
    while True:
        trigPin.value(0)
        time.sleep_us(5)
        trigPin.value(1)
        time.sleep_us(TRIG_PULSE_DURATION_US)
        trigPin.value(0)
        
        ultrasonic_duration = time_pulse_us(echoPin,1,30000)
        distance_cm = SOUND_SPEED * ultrasonic_duration / 20000
        
        print(f'Distance: {distance_cm}cm')
        time.sleep_ms(500)
except KeyboardInterrupt:
    print("The program has been terminated.")
