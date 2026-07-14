import time
from motor import MOTOR
from machine import Pin, PWM

ENA = PWM(Pin(<Value of Pin Enable A>))
ENB = PWM(Pin(<Value of Pin Enable B>))
IN1 = Pin(<Value of Pin IN1>, mode = Pin.OUT)
IN2 = Pin(<Value of Pin IN2>, mode = Pin.OUT)
IN3 = Pin(<Value of Pin IN3>, mode = Pin.OUT)
IN4 = Pin(<Value of Pin IN4>, mode = Pin.OUT)
ENA.freq(1000)
ENB.freq(1000)
DUTY = <Value between 0 - 65536>

Motor = MOTOR(IN1, IN2, IN3, IN4, ENA, ENB, DUTY)

Motor.normalforward()
print("Driving Forward...")
time.sleep(0.5)
Motor.backward()
print("Driving Backwards...")
time.sleep(0.5)
Motor.leftturn()
print("Turning Left...")
time.sleep(0.5)
Motor.rightturn()
print("Turning Right...")
time.sleep(0.5)
Motor.stop()
print("Stopping...")
print("Test Completed Successfully!")

