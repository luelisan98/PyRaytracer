from rayTracer.rays import Rays
from rayTracer.tuples import Tuples

import math

EPSILON = 0.00001

class Intersection():
	def __init__(self,t=None,obj=None):
		self.t = t
		self.obj = obj

	def to_str(self):
		return "t: " + str(self.t), "obj: " + self.obj.to_str()

	def intersections(*intersections):
		v = []
		for i in intersections:
			if i.t is not None and i.obj is not None:
				v.append(i)
		return v

	def __eq__(self, other):
		return self.t == other.t and self.obj == other.obj

	def transform(self, ray, matrix):
		new_origin = matrix * ray.origin
		new_direction = matrix * ray.direction 
		return Rays(new_origin, new_direction)
	
	def intersect(self, obj, ray):
		ray2 = self.transform(ray, obj.transform.inverse())
		sphere_to_ray = ray2.origin - Tuples().Point(0, 0, 0)
		a = Tuples().Vector(ray2.direction.x,ray2.direction.y,ray2.direction.z)
		a = a.dot(ray2.direction)
		b = Tuples().Vector(ray2.direction.x,ray2.direction.y,ray2.direction.z)
		b = b.dot(sphere_to_ray)
		b = 2 * b
		c = Tuples().Vector(sphere_to_ray.x,sphere_to_ray.y,sphere_to_ray.z)
		c = c.dot(sphere_to_ray) - 1
		discriminant = b**2 - 4 * a * c
		z = []
		if discriminant >= 0:
			t1 = (-b - math.sqrt(discriminant)) / (2 * a)
			t2 = (-b + math.sqrt(discriminant)) / (2 * a)
			z.append(Intersection(t1,obj))
			z.append(Intersection(t2,obj))
		return z
	
	def hit(self,intersections):
		hit_list = [intersection for intersection in intersections if intersection.t >= 0]
		if not hit_list:
				return None
		return min(hit_list, default=None)
		
	def __lt__(self, other):
		return self.t < other.t
	
	def intersect_world(self, world, ray):
		intersections = []
		h = []
		for obj in world.objects:
			h = obj.intersect(ray)
			intersections.extend(h)
		intersections.sort(key=lambda x: x.t)
		return intersections