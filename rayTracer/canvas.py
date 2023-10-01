from rayTracer.colors import Colors

class Canvas():
	def __init__(self, w, h, color = Colors(0,0,0)):
		self.height = h
		self.width = w
		self.grid  = [[color for _ in range(self.height)] for _ in range(self.width)]
		print(color)
		
	def write_pixel(self, x,y, Color):
		self.grid[x][y] = Color * 255

	def pixel_at(self, x, y):
		return self.grid[x][y]

	def canvas_to_ppm(self, file):
		pass

