from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.intersection import Intersection


class Computations():
	def __init__(self):
		self.t = 0
		self.object = None
		self.point = None
		self.eyev = None
		self.normalv = None
		self.inside = None
		self.over_point = Tuples().Point(0,0,0)

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
		return self
	
	def shade_hit(self, world,comps):
		return Lights().lighting(comps.object.material, world.light, comps.point, comps.eyev, comps.normalv)

	def color_at(self, world, ray):
		ints_world = Intersection().intersect_world(world, ray)
		hit = Intersection().hit(ints_world)
		if hit:
			comps = self.prepare_computations(hit,ray)
			return self.shade_hit(world, comps)
		return Colors(0,0,0)