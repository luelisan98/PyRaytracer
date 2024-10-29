
from rayTracer.shapes import Shape
from rayTracer.tuples import Tuples
from rayTracer.intersection import Intersection

EPSILON = 0.0001

class Plane(Shape):
	
	def to_str(self):
		return "Plane"

	def local_normal_at(self, point):
		return Tuples().Vector(0,1,0)
	
	def intersect(self, ray):
		local_ray =  super().intersect(ray)
		if abs(local_ray.direction.y) < EPSILON:
			return []
		t = -local_ray.origin.y / local_ray.direction.y 
		return Intersection().intersections(Intersection(t,self))
	
	def __eq__(self, other):
		return super().__eq__(other)



	def bounds(self):
	# Planes are infinite, so we use large bounding values
		min_point = Tuples().Point(float('-inf'), float('-inf'), float('-inf'))
		max_point = Tuples().Point(float('inf'), float('inf'), float('inf'))
		return [min_point, max_point]