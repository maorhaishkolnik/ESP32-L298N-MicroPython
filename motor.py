import time

class MOTOR:
 
 def __init__(self, in1, in2, in3, in4, ena, enb, duty):
     self.in1 = in1
     self.in2 = in2
     self.in3 = in3
     self.in4 = in4
     self.ena = ena
     self.enb = enb
     self.duty = duty
     
 def set_speed(self, leftfix = CALI1 , rightfix = CALI2 ): #change the CALI1 and CALI2 according to your calibration, in order to succeed change the CAL1 and CAL2 slightly from 1.0 and see what works for you. for default setting change both values to 1.0.
     self.ena.duty_u16(int(self.duty * leftfix))
     self.enb.duty_u16(int(self.duty * rightfix))

 def forward(self):
    self.in1.value(1)
    self.in2.value(0)
    self.in3.value(0)
    self.in4.value(1)
    
 def normalforward(self):
    self.set_speed()
    self.forward()

 def backward(self):
    self.in1.value(0)
    self.in2.value(1)
    self.in3.value(1)
    self.in4.value(0)
    
 def stop(self):
    self.in1.value(0)
    self.in2.value(0)
    self.in3.value(0)
    self.in4.value(0)
    self.ena.duty_u16(0)
    self.enb.duty_u16(0)

 def leftturn(self):
    self.set_speed()
    self.in1.value(1)
    self.in2.value(0)
    self.in3.value(1)
    self.in4.value(0)
    time.sleep(TIME) #change the TIME value between 0 - 1.0 sec and check what works best for smooth left turn.
    self.stop()
    
    
 def rightturn(self):
    self.set_speed()
    self.in1.value(0)
    self.in2.value(1)
    self.in3.value(0)
    self.in4.value(1)
    time.sleep(TIME) #change the TIME value between 0 - 1.0 sec and check what works best for smooth right turn.
    self.stop()
    
 def backturn(self):
    self.set_speed()
    self.in1.value(0)
    self.in2.value(1)
    self.in3.value(0)
    self.in4.value(1)
    time.sleep(TIME) #change the TIME value between 0 - 1.0 sec and check what works best for smooth back turn.
    self.stop()
     
 def rightfix(self):
    self.set_speed(leftfix = 1.00, rightfix = CALI) #if calibration isnt perfect, change the CALI value to best value for smooth fixing of rightfix 0.5 - 1.5 *this fucntion is optional for usage, relevant for projects of cars following black line. **if has no usage please remove all fucntion.
    self.forward()
    
 def leftfix(self):
    self.set_speed(leftfix = CALI, rightfix = 1.00) #if calibration isnt perfect, change the CALI value to best value for smooth fixing of leftfix between 0.5 - 1.5 *this fucntion is optional for usage, relevant for projects of cars following black line. **if has no usage please remove all fucntion.
    self.forward()
    
