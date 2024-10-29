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
	
	def bounds(self):
		# Assuming the sphere is centered at the origin with radius 1
		points = [
			Tuples().Point(-1, -1, -1),
			Tuples().Point(-1, -1,  1),
			Tuples().Point(-1,  1, -1),
			Tuples().Point(-1,  1,  1),
			Tuples().Point( 1, -1, -1),
			Tuples().Point( 1, -1,  1),
			Tuples().Point( 1,  1, -1),
			Tuples().Point( 1,  1,  1)
		]

		# Apply the transformation to each point
		transformed_points = [self.transform * point for point in points]

		# Calculate the min and max points from the transformed points
		min_x = min(point.x for point in transformed_points)
		min_y = min(point.y for point in transformed_points)
		min_z = min(point.z for point in transformed_points)
		max_x = max(point.x for point in transformed_points)
		max_y = max(point.y for point in transformed_points)
		max_z = max(point.z for point in transformed_points)

		min_point = Tuples().Point(min_x, min_y, min_z)
		max_point = Tuples().Point(max_x, max_y, max_z)

		return [min_point, max_point]