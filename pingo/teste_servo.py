import pingo
from pingo.parts import Servo

placa = pingo.detect.MyBoard()

p = placa.pins[9]
a = placa.pins["A0"]

servo = Servo(p)
while True:
  angulo = a.ratio() * 180
  servo.degree(angulo)
  print angulo,