
from rayTracer.tuples import Tuples

EPSILON = 0.00001

class Rays():
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction

	def position(self, t):
		return self.origin + self.direction * t
	
	def to_str(self):
		return f"Ray - Origin: {self.origin.to_str()}, Direction: {self.direction.to_str()}"

	def transform(self, transform):
		return Rays(transform * self.origin, transform * self.direction)
	
	def check_axis(self, origin, direction, min_point, max_point):
		tmin_numerator = min_point - origin
		tmax_numerator = max_point - origin
		if abs(direction) >= EPSILON:
			tmin = tmin_numerator / direction
			tmax = tmax_numerator / direction
		else:
			tmin = tmin_numerator * inf
			tmax = tmax_numerator * inf
		if tmin > tmax:
			tmin, tmax = tmax, tmin
		return tmin, tmax

	def intersects(self, bounds):
		min_point, max_point = bounds
		xtmin, xtmax = self.check_axis(self.origin.x, self.direction.x, min_point.x, max_point.x)
		ytmin, ytmax = self.check_axis(self.origin.y, self.direction.y, min_point.y, max_point.y)
		ztmin, ztmax = self.check_axis(self.origin.z, self.direction.z, min_point.z, max_point.z)
		tmin = max(xtmin, ytmin, ztmin)
		tmax = min(xtmax, ytmax, ztmax)
		return tmin <= tmax



	