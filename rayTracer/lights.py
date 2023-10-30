from rayTracer.tuples import Tuples
from rayTracer.colors import Colors

class Lights():
	def __init__(self):
		self.position = None
		self.intensity = None

	def point_light(self, position, intensity):
		self.position = position
		self.intensity = intensity
		return self

	def lighting(self, material, light, point, eyev, normalv, in_shadow=None):
		effective_color = material.color * light.intensity
		p = light.position - point
		lightv = p.normalize()
		ambient = effective_color * material.ambient
		light_dot_normal = lightv.dot(normalv)
		if light_dot_normal < 0 :
			diffuse = Colors(0,0,0)
			specular = Colors(0,0,0)
		else:
			diffuse = effective_color * material.diffuse * light_dot_normal
			reflectv = -lightv
			reflectv = reflectv.reflect(normalv)
			reflect_dot_eye = reflectv.dot(eyev)
			if reflect_dot_eye <= 0:
				specular = Colors(0,0,0)
			else:
				factor = reflect_dot_eye ** material.shininess
				specular = light.intensity * material.specular * factor

		return ambient + diffuse + specular

	def __eq__(self, other):
		return self.position == other.position and self.intensity == other.intensity
