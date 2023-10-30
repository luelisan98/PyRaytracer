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
		if self.equal(mag, 0):
			return Tuples(0, 0, 0, 0)
		else:
			return self / mag
	
	def dot(self, other, other1=None):
		if other1 != None:
			return ( other.x*other1.x ) + ( other.y*other1.y ) + ( other.z*other1.z )+ ( other.w*other1.w ) 
		else:
			return ( other.x*self.x ) + ( other.y*self.y ) + ( other.z*self.z )+ ( other.w*self.w ) 
	
	def cross(self, other):
		x =  self.y * other.z - self.z * other.y
		y = self.z * other.x - self.x * other.z
		z = self.x * other.y - self.y * other.x
		return Tuples(x,y,z,0)

	def reflect(self, normal):
		dot_product = 2 * self.dot(normal)
		reflection = self - normal * dot_product
		return reflection

	def to_str(self):
		return f"Tuples({self.x}, {self.y}, {self.z}, {self.w})"