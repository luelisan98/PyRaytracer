from rayTracer.matrix import Matrix
from rayTracer.materials import Materials
from rayTracer.intersection import Intersection
from rayTracer.tuples import Tuples

class Shape():	
	def __init__(self):
		self.transform = Matrix(4,4).identity()
		self.material = Materials()
		
	def test_shape(self):
		s = Shape()
		return s
	
	def set_transform(self, mat_transform):
		self.transform = mat_transform
	
	def intersect(self, ray):
		local_ray = ray.transform(self.transform.inverse()) 
		return self.local_intersect(local_ray)
	
	def local_intersect(self, ray):
		self.saved_ray = ray
		return self.saved_ray
	
	def object_normal(self, point):
		return Tuples().Vector(point.x,point.y,point.z)
	
	def __eq__(self, other):
		return  self.transform == other.transform \
			and self.material == other.material
	
	def local_normal_at(self,point):
		return Tuples().Vector(point.x, point.y, point.z)
	
	def normal_at(self,point):
		local_point = self.transform.inverse() * point
		local_normal = self.local_normal_at(local_point)
		inverse = self.transform.inverse() 
		world_normal = inverse.transposing() * local_normal
		world_normal.w = 0
		return world_normal.normalize()
	

	def bounds(self):
		# Return the bounding box as a tuple (min_point, max_point)
		raise NotImplementedError("Subclasses must implement this method")