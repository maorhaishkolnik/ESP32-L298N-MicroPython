import time
from motor import MOTOR
from machine import Pin, PWM

ENA = PWM(Pin(4))
ENB = PWM(Pin(5))
IN1 = Pin(13, mode = Pin.OUT)
IN2 = Pin(12, mode = Pin.OUT)
IN3 = Pin(32, mode = Pin.OUT)
IN4 = Pin(26, mode = Pin.OUT)
ENA.freq(1000)
ENB.freq(1000)
DUTY = 60000

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
