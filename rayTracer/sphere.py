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
		self.intresections = []

	def intersection(self, ray):
		ray2 = Intersection().transform(ray, self.transform.inverse())
		sphere_to_ray = ray2.origin - self.center
		a = Tuples.dot(ray2.direction, ray2.direction)
		b = 2 * Tuples.dot(ray2.direction, sphere_to_ray)
		c = Tuples.dot(sphere_to_ray, sphere_to_ray) - self.radius
		discriminant = b**2 - 4 * a * c

		if discriminant < 0:
			return None,None
		else:
			t1 = (-b - math.sqrt(discriminant)) / (2 * a)
			t2 = (-b + math.sqrt(discriminant)) / (2 * a)
			return t1,t2
		
	def set_transform(self, mat_transform):
		self.transform = mat_transform
		return self