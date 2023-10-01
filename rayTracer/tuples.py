from math import sqrt 

EPSILON = 0.00001

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
		return self

	def Vector(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		self.w = 0
		return self
	
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
		return self.equal(self.x, other.x) and \
			self.equal(self.y, other.y) and \
			self.equal(self.z, other.z) and \
			self.equal(self.w, other.w)
		
	def __mul__(self, num):
		return Tuples(self.x * num, self.y * num, self.z * num, self.w * num)

	def __truediv__(self, num):
		if num == 0:
			num = 1 
		return Tuples(self.x / num, self.y / num, self.z / num, self.w / num)
	
	def magnitude(self):
		return sqrt(self.x**2+self.y**2+self.z**2+self.w**2) 
	
	def equal(self, a, b):
		return abs(a - b) < EPSILON

	def normalize(self):
		mag = self.magnitude()
		if mag == 0:
			return Tuples(0, 0, 0, 0)
		else:
			return self / mag
	
	def dot(self, Tuple):
		return self.x * Tuple.x +\
			self.y * Tuple.y +\
			self.z * Tuple.z +\
			self.w * Tuple.w
	
	def cross(self, Tuple):
		x =  self.y * Tuple.z - self.z * Tuple.y
		y = self.z * Tuple.x - self.x * Tuple.z
		z = self.x * Tuple.y - self.y * Tuple.x
		return Tuples(x,y,z,0)

	def reflect(self, Tuple):
		pass
