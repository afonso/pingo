import pingo

import time
import threading

class Servo(object):
	def __init__(self, pin):
		pin.mode = pingo.OUT
		self.pin = pin

	def degree(self, value):
		micro_seconds = (value * (2350 - 500) / 180 + 500) / 10000000.0
		self.pin.high()
		time.sleep(micro_seconds)
		self.pin.low()
		time.sleep(0.4 - micro_seconds)
		time.sleep(0.2 / 1000.0)