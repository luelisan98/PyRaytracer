from rayTracer.colors import Colors

class Materials():
	def __init__(self):
		self.color = Colors(1,1,1)
		self.ambient = 0.1
		self.diffuse = 0.9
		self.specular = 0.9
		self.shininess = 200.0

	def __eq__(self, other):
		return (self.color == other.color) and \
				(self.ambient == other.ambient) and \
				(self.diffuse == other.diffuse) and \
				(self.specular == other.specular) and \
				(self.shininess == other.shininess)