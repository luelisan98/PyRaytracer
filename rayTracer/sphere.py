from rayTracer.tuples import Tuples
from rayTracer.matrix import Matrix
from rayTracer.intersection import Intersection
from rayTracer.materials import Materials
import math
import uuid

EPSILON = 0.00001

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
	
	def to_str(self):
		return f"Sphere ID: {self.id}, Center: {self.center.to_str()}, Radius: {self.radius}, Transform: {self.transform.mat}, Material: {self.material.to_str()}"

	def equal(self, a, b):
		return abs(a - b) < EPSILON

	def __eq__(self, other):
		return self.center == other.center \
			and self.equal(self.radius, other.radius) \
			and self.transform == other.transform \
			and self.material == other.material