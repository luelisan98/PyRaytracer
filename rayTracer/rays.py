from rayTracer.tuples import Tuples

class Rays():
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction

	def position(self, t):
		return self.origin + self.direction * t
	
	def to_str(self):
		return f"Ray - Origin: {self.origin.to_str()}, Direction: {self.direction.to_str()}"

	def transform(self, transform):
		return Rays(transform * self.origin, transform * self.direction)