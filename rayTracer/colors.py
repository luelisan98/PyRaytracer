from rayTracer.tuples import Tuples

class Colors(Tuples):
	def __init__(self, red, green, blue, w=None):
		super().__init__(red, green, blue, w)
		self.r = red
		self.g = green
		self.b = blue

	def __add__(self, other):
		return super().__add__(other)
	
	def __sub__(self,other):
		return super().__sub__(other)
	
	def __mul__(self, num):
		return super().__mul__(num)