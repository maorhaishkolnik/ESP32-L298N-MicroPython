# ESP32 L298N Motor Library

A lightweight MicroPython library for controlling two DC motors using an ESP32 and the L298N motor driver.

This library was originally developed as part of my high school final electronics project. After successfully using it in my own robot, I decided to publish it as open source so future students and hobbyists could easily use it in their own projects.

---

## Features

- Forward movement
- Backward movement
- Left turn
- Right turn
- Stop
- PWM speed control
- Independent motor calibration
- Simple and lightweight API

---

## Hardware

Designed for:

- ESP32
- L298N Motor Driver
- Two DC Motors
- MicroPython

---

# ⚠ Important - Motor Calibration

Every pair of DC motors is slightly different.

Because of manufacturing tolerances, one motor may spin faster than the other even when both receive the same PWM value.

For this reason, **the library includes calibration variables that should be adjusted before using the robot.**

Inside `motor.py` you will find values similar to:

```python
LEFT_FIX = ...
RIGHT_FIX = ...
```

Adjust these values until the robot drives straight when moving forward.

Usually this calibration only needs to be done once for each robot.

---

## Wiring

Example GPIO configuration:

| ESP32 | L298N |
|-------|-------|
| GPIO26 | IN1 |
| GPIO27 | IN2 |
| GPIO25 | IN3 |
| GPIO33 | IN4 |
| GPIO14 | ENA |
| GPIO32 | ENB |

Modify the pin numbers if your hardware is different.

---

## Installation

1. Copy `motor.py` to your ESP32.
2. Adjust the GPIO pins if necessary.
3. Perform motor calibration.
4. Import the library into your project.

```python
from motor import Motor
```

---

## Quick Example

```python
from motor import MOTOR

Motor = Motor(...)

Motor.forward()
Motor.leftturn()
Motor.rightturn()
Motor.backward()
Motor.stop()
```

---

## Example Programs

Examples included in this repository:

- Basic movement test
- Motor calibration
- Square driving demo

---

## Future Improvements

- Additional examples
- Better documentation
- Support for more motor drivers
- More configurable speed profiles

---

## License

This project is licensed under the MIT License.

---

## Author

**Maor Hai Shkolnik**

If this library helped your project, consider giving the repository a ⭐.
