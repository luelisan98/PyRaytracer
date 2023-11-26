from rayTracer.lights import Lights
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.sphere import Sphere
from rayTracer.transformations import Transformations
from rayTracer.materials import Materials
from rayTracer.rays import Rays
from rayTracer.intersection import Intersection

class World():
	def __init__(self):
		self.light = Lights()
		self.objects = []

	def default_world(self):
		s1 = Sphere()
		s2 = Sphere()

		point = Tuples().Point(-10, 10, -10)
		color = Colors(1, 1, 1)
		self.light.point_light(point, color)

		material = Materials()
		material_color = Colors(0.8, 1.0, 0.6)
		material.color = material_color
		material.diffuse = 0.7
		material.specular = 0.2

		s1 = Sphere()
		s1.material = material
	
		trans = Transformations()
		s2 = Sphere()
		s2.set_transform(trans.scaling(0.5, 0.5, 0.5))

		self.objects.append(s1)
		self.objects.append(s2)
		return self
	
	def is_shadowed(self,p):
		result = False
		v = self.light.position - p
		distance = v.magnitude()
		direction = v.normalize()
		r = Rays(p, direction)
		intersections = Intersection().intersect_world(self, r)
		h = Intersection().hit(intersections)
		if h and h.t < distance:
			result =  True
		else:
			result = False
		return result

	def __eq__(self, other):
		return self.light == other.light and self.objects == other.objects
	