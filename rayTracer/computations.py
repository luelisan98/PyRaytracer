from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.intersection import Intersection
from rayTracer.worlds import World
from rayTracer.rays import Rays

EPSILON = 0.0001

class Computations():
	def __init__(self):
		self.t = 0
		self.object = None
		self.point = None
		self.eyev = None
		self.normalv = None
		self.inside = None
		self.reflectv = None
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

		self.reflectv = r.direction.reflect(self.normalv)
		self.over_point = self.point + self.normalv * EPSILON
		return self
	
	def shade_hit(self, world,comps):
		comps.in_shadow =  world.is_shadowed(comps.over_point)
		return Lights().lighting(comps.object.material, comps.object, world.light, comps.point, comps.eyev, comps.normalv, comps.in_shadow)

	def color_at(self, world, ray):
		ints_world = Intersection().intersect_world(world, ray)
		hit = Intersection().hit(ints_world)
		if hit:
			print(hit.t, hit.obj)
			comps = self.prepare_computations(hit,ray)
			return self.shade_hit(world, comps)
		return Colors(0,0,0)
	
	def reflected_color(self, world):
		if self.object.material.reflective == 0:
			return Colors(0,0,0)
			
		reflected_ray = Rays(self.over_point, self.reflectv)
		color = self.color_at(world, reflected_ray)
		print("reflected color:", color, self.object.material.reflective, self.object)
		return color * self.object.material.reflective