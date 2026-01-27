from M04_DCMotor_Module import DCMotor
from M05_Steering_Motor_Module import SteeringMotor
import time

dcMotor = DCMotor(1,0)
steeringMotor = SteeringMotor(7)

dcMotor.rotateForward()
steeringMotor.turnForward()
time.sleep(3)

dcMotor.rotateForward()
steeringMotor.turnLeft()
time.sleep(3)

dcMotor.rotateForward()
steeringMotor.turnLeft()
time.sleep(3)

dcMotor.stop()
steeringMotor.turnForward()
time.sleep(3)

dcMotor.rotateBackward()
steeringMotor.turnForward()
time.sleep(3)

dcMotor.rotateBackward()
steeringMotor.turnleft()
time.sleep(3)

dcMotor.rotateBackward()
steeringMotor.turnRight()
time.sleep(3)

dcMotor.stop()
steeringMotor.turnForward()
