from machine import Pin,PWM



# This file is required to be run for the project to be completed.


class ServoMotor:
    
    MIN_ANGLE=1600
    MAX_ANGLE=7900
    MID_ANGLE=(MIN_ANGLE+MAX_ANGLE)//2
    DEGREE_1=(MAX_ANGLE-MIN_ANGLE)//180
    
    def __init__(self,pwm):
        self.pwm=PWM(Pin(pwm))
        self.pwm.freq(50)

    def setDutyCycle(self,position):
        self.pwm.duty_u16(position)
    
    def setAngle(self, angle):
        if 0<=int(angle)<=180:
            self.setDutyCycle(self.MIN_ANGLE+self.DEGREE_1*angle)

# After turning on both the board and the motor power,
# you must run it once for each motor
# by replacing the “7” in ServoMotor(7) with the motor’s pin number.
if __name__=='__main__':
    
    import time
    
    servoMotor=ServoMotor(7)
    
    servoMotor.setAngle(90)
