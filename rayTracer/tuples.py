from math import sqrt 

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
		
	def __add__(self, other):
		return Tuples(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

	def __sub__(self, other):
		return Tuples(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

	def __neg__(self):
		return Tuples(-self.x, -self.y, -self.z, -self.w)
	
	def __eq__(self, other):
		return self.x == other.x and \
			self.y == other.y and \
			self.z == other.z and \
			self.w == other.w
		
	def __mul__(self, num):
		return Tuples(self.x * num, self.y * num, self.z * num, self.w * num)

	def __truediv__(self, num):
		if num == 0:
			num = 1 
		return Tuples(self.x / num, self.y / num, self.z / num, self.w / num)
	
	def magnitude(self, Tuple):
		return sqrt(Tuple.x**2+Tuple.y**2+Tuple.z**2+Tuple.w**2) 

	def equal(self, result, expected):
		return result == expected
	
	def normalize(self, Tuple):
		mag = self.magnitude(Tuple)
		if mag == 0:
			return Tuples(0, 0, 0, 0)
		else:
			return Tuple / mag
	
	def dot(self, Tuple, other):
		return Tuple.x * other.x +\
			Tuple.y * other.y +\
			Tuple.z * other.z +\
			Tuple.w * other.w
	
	def cross(self, Tuple, other):
		x =  Tuple.y * other.z - Tuple.z * other.y
		y = Tuple.z * other.x - Tuple.x * other.z
		z = Tuple.x * other.y - Tuple.y * other.x
		return Tuples(x,y,z,0)	
		
	def reflect(self):
		pass