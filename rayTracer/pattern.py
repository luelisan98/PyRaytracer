from rayTracer.colors import Colors
from rayTracer.matrix import Matrix

import math

class Pattern():
	def __init__(self):
		self.transform = Matrix(4,4).identity()

	def stripe_pattern(self, color1, color2):
		self.a = color1
		self.b = color2 
		return self

	def stripe_at(self, point):
		if math.floor(point.x) % 2 == 0:
			return self.a 
		else: 
			return self.b
		
	def __eq__(self, other):
		return (
			self.transform == other.transform and
			self.a == other.a and
			self.b == other.b )

	