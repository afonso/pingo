import pingo

import time
import threading

class Servo(object):
	def __init__(self, pin):
		pin.mode = pingo.OUT
		self.pin = pin

	def degree(self, value):
		micro_seconds = (value * (2350 - 500) / 180 + 500) / 1000000.0
		self.pin.high()
		time.sleep(micro_seconds)
		self.pin.low()
		time.sleep(micro_seconds)