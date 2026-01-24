from M03_ServoMotor_Module import ServoMotor

class SteeringMotor(ServoMotor):
    def __init__(self,pwm):
        super().__init__(pwm)
        
    def turnLeft(self):
        self.setAngle(0)
        
    def turnForward(self):
        self.setAngle(int(90*0.85))
        
    def turnRight(self):
        self.setAngle(180)
        
        