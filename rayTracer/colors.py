EPSILON = 0.00001

from math import ceil

class Colors():
	def __init__(self, red =0, green=0, blue=0):
		self.r = red
		self.g = green
		self.b = blue

	def equal(self, a, b):
		return abs(a - b) < EPSILON

	def __add__(self, other):
		return Colors(self.r + other.r, self.g + other.g, self.b + other.b)
	
	def __eq__(self, other):
		return self.equal(self.r, other.r) and \
			self.equal(self.g, other.g) and \
			self.equal(self.b, other.b) 
	
	def __sub__(self,other):
		return Colors(self.r - other.r, self.g - other.g, self.b - other.b)

	def __mul__(self,other):
		if isinstance(other, Colors):
			return Colors(self.r * other.r, self.g * other.g, self.b * other.b)
		elif isinstance(other, float):
			return Colors(self.r * other, self.g * other, self.b * other)
		elif isinstance(other, int):
			return Colors(self.r * other, self.g * other, self.b * other)
		
	def to_rgba(self):
		red = ceil(self.r * 255)
		green = ceil(self.g * 255)
		blue = ceil(self.b * 255)
		red = max(0, min(255, red))
		green = max(0, min(255, green))
		blue = max(0, min(255, blue))
		return [str(red), str(green), str(blue)]
	
	def to_str(self):
		return f"Color({self.r}, {self.g}, {self.b})"
	
	def __str__(self):
		return f"Color({self.r}, {self.g}, {self.b})"
	

	def __round__(self):
		r = round(self.r)
		g = round(self.g)
		b = round(self.b)
		return Colors(r,g,b)