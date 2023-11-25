from rayTracer.colors import Colors
from rayTracer.matrix import Matrix

import math

class Pattern():
	def __init__(self):
		self.transform = Matrix(4,4).identity()

	def test_pattern(self):
		p = Pattern()
		return p

	def pattern_at_shape(self, obj, world_point):
		object_point = obj.transform.inverse() * world_point
		pattern_point = self.transform.inverse() * object_point
		return self.pattern_at(pattern_point)
	
	def set_pattern_transform(self, transformation):
		self.transform = transformation

	def __eq__(self, other):
			return (
				self.transform == other.transform and
				self.a == other.a and
				self.b == other.b )


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
	

class Gradient(Pattern):
	def __init__(self, color1, color2):
		super().__init__()
		self.a = color1
		self.b = color2
	
	def pattern_at(self,point):
		distance = self.b - self.a 
		fraction = point.x - math.floor(point.x)
		return self.a + distance * fraction

class Ring(Pattern):
	def __init__(self, color1, color2):
		super().__init__()
		self.a = color1
		self.b = color2

	def pattern_at(self, point):
		in_ring = math.floor(math.sqrt((point.x ** 2) + (point.z ** 2))) % 2 == 0
		if in_ring:
			return self.a 
		else:
			return self.b
		
class Checker(Pattern):
	def __init__(self, color1, color2, uv_map = False):
		super().__init__()
		self.a = color1
		self.b = color2
		self.uv_map = uv_map

	def pattern_at(self,point):
		if self.uv_map is True:
			theta = math.atan2(point.x, point.z) + math.pi
			r = point.magnitude()
			phi = math.acos(point.y / r)
			u = theta / (2 * math.pi)
			v = phi / math.pi
			if (math.floor(u * 20) + math.floor(v * 10)) % 2 == 0:
				return self.a
			return self.b

		in_check = (math.floor(point.x) + math.floor(point.y) + math.floor(point.z)) % 2 == 0
		if in_check is True:
			return self.a
		return self.b