from rayTracer.colors import Colors

from math import ceil

class Canvas():
	def __init__(self, w, h, color = Colors(0,0,0)):
		self.height = h
		self.width = w
		self.grid  = [[color for _ in range(self.height)] for _ in range(self.width)]

	def write_pixel(self, x,y, Color):
		self.grid[x][y] = Color

	def pixel_at(self, x, y):
		return round(self.grid[x][y] * 255)

	def canvas_to_ppm(self, file_path):
		with open(file_path, 'w') as file:
			file.write("P3\n")
			file.write(f"{self.width} {self.height}\n")
			file.write("255\n")
			for row in range(self.height):
				ppm_row = []
				for col in range(self.width):
					# Access the element at the current row and column
					element = self.pixel_at(col, row)
					red = ceil(element.r)
					green = ceil(element.g)
					blue = ceil(element.b)

					red = max(0, min(255, red))
					green = max(0, min(255, green))
					blue = max(0, min(255, blue))

					ppm_row.extend([red, green, blue])
					
				# break into at most 17 elements per line to stay < 70 chars
				for line in [ppm_row[i: i + 17] for i in range(0, len(ppm_row), 17)]:
					file.write(" ".join(str(c) for c in line) + " ")
				file.write("\n")

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