ESP32 Motor Library for MicroPython
Created by Maor Hai Shkolnik

Introduction:

Designed for MicroPython and the L298N motor driver.
This library was originally developed as part of a high-school Electronics and Computer Engineering project
and is released as open source so future students can use, improve and learn from it.

Tutorial:

In the Motor Library there are 7 functions for usage.
the functions featured in  the library are:
- normalforward - for driving forward
- backward - for driving backwards
- stop - for stop driving 
- leftturn - for turning left
- rightturn - for turning right
- backturn - for turning back (turn 180 degrees)
- rightfix - for slightly driving left *optional depending on task
- leftfix - for slightly driving right *optional depending on task

In order to use the library the user needs to upload the library file "motor.py" into the ESP32 Storage, and in the Main code
to set the library with his own parameters, the library needs to detect from the user 7 parameters.
also, please change the time and calibration for your own project, every wheel can be different, therfore you would need to change some paramters in the library according to your project,
please check the code of the library and read all the marks I have written for you and to what value to set.
list of parameters needed:
- IN1 - Pin of IN1
- IN2 - Pin of IN2
- IN3 - Pin of IN3
- IN4 - Pin of IN4 
- Ena - Pin of Enable A for PWM (Engine left)
- Enb - Pin of Enable B for PWM (Engine Right)
- Duty - Value of bits that the Engine will be turned on, the value should be between 0 - 65536,
the lower the value of duty the slower the speed of the wheels will be. in order to understand it better,
learn about PWM.

In order to see how the library works in real time, check out the "Examples" folder, I have Uploaded to there
real life usage of the code, I have uploaded also a test file in order for you to check if it works for you.

Also, I have added "Calibration.py", this code will help you do the calibration test needed in order to do calibration and check the values needed for yourself.

if everything is working then good luck with your project and have fun with it! :-) 
