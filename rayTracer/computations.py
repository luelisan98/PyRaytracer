from rayTracer.tuples import Tuples

class Computations():
	def __init__(self):
		self.t = 0
		self.object = None
		self.point = None
		self.eyev = None
		self.normalv = None
		self.inside = None
		self.over_point = Tuples().Point(0,0,0)

	def prepare_computations(self,i,r):
		self.t = i.t
		self.object = i.obj
		self.point = r.position(self.t)
		self.eyev = -r.direction  
		self.normalv = self.object.normal_at(self.point)
		if self.normalv.dot(self.eyev):
			self.inside = True
			self.normalv = -self.normalv
		else:
			self.inside = False
		return self