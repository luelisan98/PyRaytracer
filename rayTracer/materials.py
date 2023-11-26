from rayTracer.colors import Colors
from rayTracer.tuples import Tuples

EPSILON = 0.00001

class Materials():
	def __init__(self):
		self.color = Colors(1,1,1)
		self.ambient = 0.1
		self.diffuse = 0.9
		self.specular = 0.9
		self.shininess = 200.0
		self.reflective = 0.0
		self.pattern = None 

	def equal(self, a, b):
		return abs(a - b) < EPSILON

	def __eq__(self, other):
		return (
			self.color == other.color
			and self.equal(self.ambient, other.ambient)
			and self.equal(self.diffuse, other.diffuse)
			and self.equal(self.specular, other.specular)
			and self.equal(self.shininess, other.shininess)
			and self.pattern == other.pattern 
			and self.equal(self.reflective, other.reflective)
		)
	
	def to_str(self):
		return f"Material - Color: {self.color.to_str()}, Ambient: {self.ambient}, Diffuse: {self.diffuse}, Specular: {self.specular}, Shininess: {self.shininess}, Reflective: {self.reflective}"
