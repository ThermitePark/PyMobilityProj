from M04_DCMotor_Module import DCMotor
from M05_Steering_Motor_Module import SteeringMotor
import time

class RCCar:
    def __init__(self,dcMotor,steeringMotor):
        self.dcMotor = dcMotor
        self.steeringMotor = steeringMotor
        
    def goForward(self):
        self.dcMotor.rotateForward()
        self.steeringMotor.turnForward()
    def goForwardLeft(self):
        self.dcMotor.rotateForward()
        self.steeringMotor.turnLeft()
    def goForwardRight(self):
        self.dcMotor.rotateForward()
        self.steeringMotor.turnLeft()
    def goBackward(self):
        self.dcMotor.rotateBackward()
        self.steeringMotor.turnForward()
    def goBackwardLeft(self):
        self.dcMotor.rotateBackward()
        self.steeringMotor.turnLeft()
    def goBackwardRight(self):
        self.dcMotor.rotateBackward()
        self.steeringMotor.turnRight()
    def stop(self):
        self.dcMotor.stop()
        self.steeringMotor.turnForward()
        