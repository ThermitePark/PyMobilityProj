from machine import Pin

class DCMotor:
    def __init__(self, P1,P2):
        self.P1 = Pin(P1,Pin.OUT)
        self.P2 = Pin(P2,Pin.OUT)
        
    def rotateForward(self):
        self.P1.value(1)
        self.P2.value(0)
        
    def rotateBackward(self):
        self.P1.value(0)
        self.P2.value(1)
        
    def stop(self):
        self.P1.value(0)
        self.P2.value(0)
        