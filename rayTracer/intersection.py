from rayTracer.rays import Rays

class Intersection():
	def __init__(self,t=None,obj=None):
		self.t = t
		self.obj = obj

	def intersections(*intersections):
		intersections = [Intersection(intersection.t, intersection.obj) for intersection in intersections]
		intersections.sort()
		return intersections

	def __eq__(self, other):
		return self.t == other.t and self.obj.id == other.obj.id

	def transform(self, ray, matrix):
		new_origin = matrix * ray.origin
		new_direction = matrix * ray.direction 
		return Rays(new_origin, new_direction)
	
	def intersect(self, obj, ray):
		t1,t2 = obj.intersection(ray)
		if t1 is None and t2 is None:
			return []
		return [Intersection(t1,obj), Intersection(t2,obj)]
	
	def hit(self,intersections):
		hit_list = [intersection for intersection in intersections if intersection.t >= 0]
		if not hit_list:
				return None
		return min(hit_list, default=None)
		
	def __lt__(self, other):
		return self.t < other.t
	