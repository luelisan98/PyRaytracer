from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.intersection import Intersection

EPSILON = 0.0001

class Computations():
	def __init__(self):
		self.t = 0
		self.object = None
		self.point = None
		self.eyev = None
		self.normalv = None
		self.inside = None
		self.over_point = Tuples().Point(0,0,0)
		self.in_shadow = False

	def prepare_computations(self,i,r):
		self.t = i.t
		self.object = i.obj
		self.point = r.position(self.t)
		self.eyev = -r.direction  
		self.normalv = self.object.normal_at(self.point)
		if self.normalv.dot(self.eyev) < 0:
			self.inside = True
			self.normalv = -self.normalv
		else:
			self.inside = False

		self.over_point = self.point + self.normalv * EPSILON
		return self
	
	def shade_hit(self, world,comps):
		if world.is_shadowed(comps.over_point):
			comps.in_shadow = True
		return Lights().lighting(comps.object.material, world.light, comps.point, comps.eyev, comps.normalv, comps.in_shadow)

	def color_at(self, world, ray):
		ints_world = Intersection().intersect_world(world, ray)
		hit = Intersection().hit(ints_world)
		if hit:
			comps = self.prepare_computations(hit,ray)
			return self.shade_hit(world, comps)
		return Colors(0,0,0)