from rayTracer.tuples import Tuples
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
		
	def to_str(self):
		return "Sphere"

	def __eq__(self, other):
		return Shape.__eq__(self,other)
	
	def intersect(self, ray):
		local_ray = super().intersect(ray)
		sphere_to_ray = local_ray.origin - Tuples().Point(0, 0, 0)

		a = local_ray.direction.dot(local_ray.direction)
		b = 2 * local_ray.direction.dot(sphere_to_ray)
		c = sphere_to_ray.dot(sphere_to_ray) - 1

		discriminant = b**2 - 4 * a * c
		z = []
		if discriminant >= 0:
			t1 = (-b - math.sqrt(discriminant)) / (2 * a)
			t2 = (-b + math.sqrt(discriminant)) / (2 * a)
			z.append(Intersection(t1,self))
			z.append(Intersection(t2,self))
		return z
	
	def glass_sphere(self):
		self.material.transparency = 1.0 
		self.material.refractive_index = 1.5
		return self