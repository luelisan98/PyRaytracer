from rayTracer.tuples import Tuples
from rayTracer.matrix import Matrix
from rayTracer.intersection import Intersection
from rayTracer.materials import Materials
import math
import uuid

class Sphere():	
	def __init__(self, center=Tuples().Point(0, 0, 0), radius=1):
		self.id = uuid.uuid4()
		self.center = center
		self.radius = radius
		self.transform = Matrix(4,4).identity()
		self.material = Materials()
		
	def set_transform(self, mat_transform):
		self.transform = mat_transform
		return self
		
	def normal_at(self, world_point):
		object_point = self.transform.inverse() * world_point
		object_normal = object_point - Tuples().Point(0,0,0)
		world_normal = self.transform.inverse().transposing() * object_normal
		world_normal.w = 0
		return world_normal.normalize()