from rayTracer.matrix import Matrix
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from rayTracer.canvas import Canvas
from rayTracer.computations import Computations

from tqdm import tqdm

import time
import math

EPSILON = 0.00001

def equals(a,b):
    if abs(a-b) < EPSILON:
        return True
    return False

class Camera():
	def __init__(self,hsize,vsize, field_of_view):
		self.hsize = hsize
		self.vsize = vsize
		self.field_of_view = field_of_view
		self.transform = Matrix(4,4).identity()
		self.pixel_size = 0.0	
		self.half_width = 0
		self.half_height = 0
		half_view = math.tan(self.field_of_view / 2)
		aspect = self.hsize / self.vsize
		if aspect >= 1:
			self.half_width = half_view
			self.half_height = half_view / aspect
		else:
			self.half_width = half_view * aspect
			self.half_height = half_view

		self.pixel_size = (self.half_width * 2) / self.hsize

	def ray_for_pixel(self, px, py):
		xoffset = (px + 0.5) * self.pixel_size
		yoffset = (py + 0.5) * self.pixel_size

		world_x = self.half_width - xoffset
		world_y = self.half_height - yoffset

		pixel = self.transform.inverse() * Tuples().Point(world_x, world_y, -1)
		origin = self.transform.inverse() * Tuples().Point(0,0,0)
		direction = pixel - origin
		direction = direction.normalize()

		return Rays(origin, direction)
	
	def render(self,w):
		start_time = time.time()
		progress_bar = tqdm(total=self.hsize * self.vsize, desc="Processing")
		image = Canvas(self.hsize, self.vsize)
		com = Computations()

		for y in range(0, self.vsize):
			for x in range(0, self.hsize):
				ray = self.ray_for_pixel(x,y)
				color = com.color_at(w, ray)
				image.write_pixel(x,y,color)
				progress_bar.update(1)
		progress_bar.close()
		end_time = time.time()
		print(f"Rendering completed in {end_time - start_time:.2f} seconds")

		return image