import pingo
from pingo.parts import Servo

arduino = pingo.arduino.get_arduino()

p = arduino.pins[9]

servo = Servo(p)
while True:
	servo.degree(90)