class Tuples:
	def __init__(self):
		pass
	
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