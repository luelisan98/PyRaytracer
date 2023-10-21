from rayTracer.tuples import Tuples
from rayTracer.matrix import Matrix
from rayTracer.intersection import Intersection
import math
import uuid

class Sphere():	
	def __init__(self, center=Tuples().Point(0, 0, 0), radius=1):
		self.id = uuid.uuid4()
		self.center = center
		self.radius = radius
		self.transform = Matrix(4,4).identity()
		
	def set_transform(self, mat_transform):
		self.transform = mat_transform
		return self
		
	def normal_at(self, world_point):
		# print(self.transform.mat)
		# print(self.transform.inverse().mat)
		object_point = self.transform.inverse() * world_point
		# print(object_point.x, object_point.y, object_point.z)
		object_normal = object_point - Tuples().Point(0,0,0)
		# print(object_normal.x, object_normal.y, object_normal.z)
		world_normal = self.transform.inverse().transposing() * object_normal
		# print(world_normal.x, world_normal.y, world_normal.z)
		world_normal.w = 0


		return world_normal.normalize()