from rayTracer.colors import Colors

from math import ceil
from io import StringIO

class Canvas():
	def __init__(self, w, h, color = Colors(0,0,0)):
		self.height = h
		self.width = w
		self.grid  = [[color for _ in range(self.height)] for _ in range(self.width)]

	def write_pixel(self, x,y, Color):
		self.grid[x][y] = Color

	def pixel_at(self, x, y):
		return round(self.grid[x][y] * 255)

# Adapted from: https://www.superperfundo.dev/articles/ray-tracer-part1 
	def canvas_to_ppm(self, file_path):
		builder = StringIO()
		builder.write("P3\n")
		builder.write(f"{self.width} {self.height}\n")
		builder.write("255\n")
		
		for y in range(self.height):
			line_length = 0
			for x in range(self.width):
				color_a = self.grid[x][y].to_rgba()
				for color in color_a:
					if line_length + 1 + len(color) > 70:
						builder.write("\n")
						line_length = 0
					if line_length != 0:
						builder.write(" ")
						line_length += 1
					builder.write(color)
					line_length += len(color)
			builder.write("\n")
		
			with open(file_path, 'w') as f:
				f.write(builder.getvalue())

	def __str__(self):
		lines = []
		for row in range(self.height):
			ppm_row = []
			for col in range(self.width):
				element = self.pixel_at(col, row)
				red = ceil(element.r)
				green = ceil(element.g)
				blue = ceil(element.b)

				red = max(0, min(255, red))
				green = max(0, min(255, green))
				blue = max(0, min(255, blue))

				ppm_row.extend([red, green, blue])

			for line in [ppm_row[i: i + 17] for i in range(0, len(ppm_row), 17)]:
				lines.append(" ".join(str(c) for c in line) + " ")
			lines.append("\n")

		return "".join(lines)