from machine import Pin, PWM

class ServoMotor:
    #Adjust MIN_ANGLE according to the motor you have
    #Adjust MAX_ANGLE according to the motor you have
    MIN_ANGLE = 1300 
    MAX_ANGLE = 8000
    MID_ANGLE = (MIN_ANGLE+MAX_ANGLE)//2
    DEGREE_1 = (MAX_ANGLE - MIN_ANGLE)//180
    # DEGREE_1 => PWM increment per 1 degree
    def __init__(self,pwm):
        self.pwm = PWM(Pin(pwm))
        self.pwm.freq(50)
        
    def setDutyCycle(self,position):
        self.pwm.duty_u16(position)
        
    def setAngle(self, angle):
        if 0<= int(angle) <= 180:
            self.setDutyCycle(self.MIN_ANGLE + self.DEGREE_1*angle)