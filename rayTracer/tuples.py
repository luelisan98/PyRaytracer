class Tuples:
	def __init__(self, x=None, y=None, z=None, w=None):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		
	def Point(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		self.w = 1

	def Vector(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		self.w = 0
	
	def isPoint(self):
		if self.w == 1:
			return True
		else:
			return False

	def isVector(self):
		if self.w == 0:
			return True
		else:
			return False
		
	def __add__(self, Tuples):
		tuple = type(Tuples)
		tuple.x = self.x + Tuples.x
		tuple.y = self.y + Tuples.y 
		tuple.z = self.z + Tuples.z 
		tuple.w = self.w + Tuples.w 
		return tuple
	
	def __sub__(self, Tuples):
		tuple = type(Tuples)
		tuple.x = self.x - Tuples.x
		tuple.y = self.y - Tuples.y 
		tuple.z = self.z - Tuples.z 
		tuple.w = self.w - Tuples.w 
		return tuple
	
	def __neg__(self):
		self.x = self.x * -1
		self.y = self.y * -1
		self.z = self.z * -1
		self.w = self.w * -1
		return self
	
	def __eq__(self, Tuples):
		if self.x == Tuples.x and \
			self.y == Tuples.y and \
			  self.z == Tuples.z and \
				self.w == Tuples.w:
			return True
		else:
			return False 
		
	def __mul__(self, num):
		self.x = self.x * num
		self.y = self.y * num
		self.z = self.z * num
		self.w = self.w * num
		return self

	def __truediv__(self, num):
		if num == 0:
			num = 1 
		self.x = self.x / num
		self.y = self.y / num
		self.z = self.z / num
		self.w = self.w / num
		return self