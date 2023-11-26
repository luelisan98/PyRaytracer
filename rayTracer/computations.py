from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.intersection import Intersection
from rayTracer.worlds import World
from rayTracer.rays import Rays

import math

EPSILON = 0.00001

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

	def prepare_computations(self,i,r,xs=None):
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
		self.under_point = self.point - self.normalv * EPSILON
		self.n1 = self.n2 = 1

		if xs:
			containers = []
			for intersection in xs:
				if intersection == i:
					self.n1 = 1 if not (len(containers)) else containers[len(containers) - 1].material.refractive_index

				if intersection.obj in containers:
					containers.remove(intersection.obj)
				else:
					containers.append(intersection.obj)

				if intersection == i:
					self.n2  = 1 if not (len(containers)) else containers[len(containers) - 1].material.refractive_index
		return self
	
	def shade_hit(self, world,comps, remaining = 5):
		comps.in_shadow =  world.is_shadowed(comps.over_point)
		surface =  Lights().lighting(comps.object.material, comps.object, world.light, comps.point, comps.eyev, comps.normalv, comps.in_shadow)
		reflected = self.reflected_color(world, comps,remaining)
		refracted = self.refracted_color(world,comps,remaining) 
		
		material = comps.object.material 
		if material.reflective > 0 and material.transparency > 0:
			reflectance = self.schlick(comps)
			return surface + reflected * reflectance + refracted * ( 1 - reflectance)
		else:
			return surface + reflected + refracted

	def color_at(self, world, ray,remaining = 5):
		ints_world = Intersection().intersect_world(world, ray)
		hit = Intersection().hit(ints_world)
		if hit:
			comps = self.prepare_computations(hit,ray)
			return self.shade_hit(world, comps, remaining)
		return Colors(0,0,0)
	
	def reflected_color(self, world,comps,remaining = 5):

		if remaining <= 0:
			return Colors(0,0,0)
		

		if comps.object.material.reflective == 0:
			return Colors(0,0,0)
			
		reflected_ray = Rays(comps.over_point, comps.reflectv)
		color = self.color_at(world, reflected_ray, remaining -1)
		return color * comps.object.material.reflective
	
	def refracted_color(self,world,comps,remaining = 5):
		if comps.object.material.transparency == 0 or remaining <= 0:
			return Colors(0,0,0)
		
		n_ratio = comps.n1 / comps.n2 
		cosi = comps.eyev.dot(comps.normalv)
		sin2t = n_ratio ** 2 * (1 - cosi ** 2)
		if sin2t > 1 :
			return Colors(0,0,0)
		cost = math.sqrt(1 - sin2t)
		direction = comps.normalv * (n_ratio * cosi - cost) - comps.eyev * n_ratio
		refracted_ray = Rays(comps.under_point, direction)
		return self.color_at(world, refracted_ray, remaining - 1) * comps.object.material.transparency
	
	def schlick(self,comps):
		cos = comps.eyev.dot(comps.normalv)
		if comps.n1 > comps.n2:
			n = comps.n1 / comps.n2 
			sin2t = n**2 * (1.0 - cos**2)
			if sin2t > 1.0:
				return 1.0
			
			cost = math.sqrt(1 - sin2t)
			cos = cost
		
		rtheta = ((comps.n1 - comps.n2) / (comps.n1 + comps.n2)) ** 2
		return rtheta + (1 - rtheta) * (1-cos) ** 5