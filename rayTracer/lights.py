from rayTracer.tuples import Tuples
from rayTracer.colors import Colors

class Lights():
	def __init__(self):
		self.position = Tuples().Point(0, 0, 0)
		self.intensity = Colors(1,1,1)

	def point_light(self, position, intensity):
		self.position = position
		self.intensity = intensity
