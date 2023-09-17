class Tuples:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		self.w = 1
	
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
	
	def __eq__(self, Tuples):
		if self.x == Tuples.x and \
		    self.y == Tuples.y and \
			  self.z == Tuples.z and \
				self.w == Tuples.w:
			return True
		else:
			return False 