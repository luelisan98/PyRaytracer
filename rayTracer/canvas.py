from rayTracer.colors import Colors

from math import ceil

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

	def canvas_to_ppm(self, file_path):
		with open(file_path, 'w') as file:
			file.write("P3\n")
			file.write(f"{self.width} {self.height}\n")
			file.write("255\n")

			# Caso donde se escribió el color y ya está en 255 
			# Caso donde no se ha escrito el color y hay que pasarlo a 255

			for row in range(self.height):
				for col in range(self.width):
					# Access the element at the current row and column
					element = self.grid[col][row]

					red = ceil(element.r)
					green = ceil(element.g)
					blue = ceil(element.b)

					# Clamp the red channel value to the [0, 255] range
					if red > 255:
						red = 255
					elif red < 0:
						red = 0

					# Clamp the green channel value to the [0, 255] range
					if green > 255:
						green = 255
					elif green < 0:
						green = 0

					# Clamp the blue channel value to the [0, 255] range
					if blue > 255:
						blue = 255
					elif blue < 0:
						blue = 0

					# Print the RGB values without newlines
					file.write(f"{red} {green} {blue} ")

				file.write("\n")