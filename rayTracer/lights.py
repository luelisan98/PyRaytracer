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

	def lighting(self, material, obj,light, point, eyev, normalv, in_shadow=False):
		if material.pattern is not None: 
			material.color = material.pattern.pattern_at_shape(obj,point)
		effective_color = material.color * light.intensity
		p = light.position - point
		lightv = p.normalize()
		ambient = effective_color * material.ambient
		light_dot_normal = lightv.dot(normalv)
		if light_dot_normal < 0 or in_shadow:
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
	
	def lighting_blinn(self, material, obj, light, point, eyev, normalv, in_shadow=False): 
		if material.pattern is not None: 
			material.color = material.pattern.pattern_at_shape(obj,point)
		effective_color = material.color * light.intensity
		p = light.position - point
		lightv = p.normalize()
		ambient = effective_color * material.ambient
		light_dot_normal = lightv.dot(normalv)
		if light_dot_normal < 0 or in_shadow:
			diffuse = Colors(0,0,0)
			specular = Colors(0,0,0)
		else:
			diffuse = effective_color * material.diffuse * light_dot_normal
		# Blinn-Phong specular calculation
			halfv = (lightv + eyev).normalize()
			half_dot_normal = max(halfv.dot(normalv), 0)
			if half_dot_normal <= 0:
				specular = Colors(0, 0, 0)
			else:
				factor = half_dot_normal ** material.shininess
				specular = light.intensity * material.specular * factor
		return ambient + diffuse + specular	

	def __eq__(self, other):
		return self.position == other.position and self.intensity == other.intensity
