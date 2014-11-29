import pingo
from pingo.parts import Servo

arduino = pingo.arduino.get_arduino()

p = arduino.pins[13]

servo = Servo(p)
while 1:
  servo.degree(30)
  print '.'