
from rayTracer.shapes import Shape
from rayTracer.tuples import Tuples
from rayTracer.intersection import Intersection

EPSILON = 0.00001

class Plane(Shape):
	def __init__(self):
		super().__init__()
	
	def local_normal_at(self, point):
		return Tuples().Vector(0,1,0)
	
	def intersect(self, ray):
		local_ray =  super().intersect(ray)
		if abs(local_ray.direction.y) < EPSILON:
			return []
		t = -local_ray.origin.y / local_ray.direction.y 
		return Intersection().intersections(Intersection(t,self))