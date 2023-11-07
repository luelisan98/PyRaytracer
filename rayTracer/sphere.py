from rayTracer.tuples import Tuples
from rayTracer.matrix import Matrix
from rayTracer.rays import Rays
from rayTracer.materials import Materials
from rayTracer.shapes import Shape
from rayTracer.intersection import Intersection
import math
import uuid

EPSILON = 0.00001

class Sphere(Shape):	
	def __init__(self):
		Shape.__init__(self)
		self.id = uuid.uuid4()

	def set_transform(self, mat_transform):
		Shape.set_transform(self,mat_transform)
		return self
		
	def normal_at(self, world_point):
		object_point = self.transform.inverse() * world_point
		object_normal = object_point - Tuples().Point(0,0,0)
		world_normal = self.transform.inverse().transposing() * object_normal
		world_normal.w = 0
		return world_normal.normalize()
	
	def __eq__(self, other):
		return Shape.__eq__(self,other)
	
	def local_intersect(self,ray):
		return Intersection.intersect(self,ray)