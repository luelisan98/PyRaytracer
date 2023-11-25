from rayTracer.colors import Colors
from rayTracer.matrix import Matrix

import math

class Pattern():
	def __init__(self):
		self.transform = Matrix(4,4).identity()

	def pattern_at_shape(self, obj, world_point):
		object_point = obj.transform.inverse() * world_point
		pattern_point = self.transform.inverse() * object_point
		return self.pattern_at(pattern_point)


class Stripe(Pattern):
		def __init__(self, color1, color2):
			super().__init__()
			self.a = color1
			self.b = color2

		def pattern_at(self, point):
			if math.floor(point.x) % 2 == 0:
				return self.a 
			else: 
				return self.b
		
		def __eq__(self, other):
			return (
				self.transform == other.transform and
				self.a == other.a and
				self.b == other.b )

	