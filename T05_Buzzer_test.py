from machine import Pin, PWM
import time

#PWM class (Pulse Width Modulation)
# .freq(value) => (value)Hz Setting
# if value =="None" => Current Frequency
# .duty_u16(value) => duty cycle Setting
# u16 => Unsigned 16bit value => 0 ~ 65535
# if value =="None" => Current Duty Cycle


buzzer = PWM(Pin(6))

buzzer.freq(262)
buzzer.duty_u16(int(65025 * 0.5))
# 65025 * 0.5 => Half High, Half Low 
# 65025 => Physical constraints of the buzzer(Max != 65535)
time.sleep(2)
buzzer.duty_u16(0)
# 0 => off

# Hearing a 2-second C note indicates normal operation.