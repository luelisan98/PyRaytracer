import sys
sys.path.append(r'C:\Users\PC\Documents\GitHub\PyRaytracer')  # Adjust this path to the actual path where project_folder is located


from rayTracer.canvas import Canvas
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.sphere import Sphere
from rayTracer.rays import Rays
from rayTracer.intersection import Intersection

ray_origin = Tuples().Point(0,0,-5)
wall_z = 10
wall_size = 7.0
canvas_pixels = 100

pixel_size = wall_size/canvas_pixels
half = wall_size / 2

canvas = Canvas(canvas_pixels, canvas_pixels)
color = Colors(0,1,0)
shape = Sphere()

intersections = []

for y in range(canvas_pixels):
	world_y = half - pixel_size * y
	for x in range(canvas_pixels):
		world_x = -half + pixel_size * x
		position = Tuples().Point(world_x, world_y, wall_z)
		a = position - ray_origin
		direction = a.normalize()
		r = Rays(ray_origin, direction)
		xs = Intersection().intersect(shape,r)
		if len(xs) > 0:
			canvas.write_pixel(x,y,color)


canvas.canvas_to_ppm("./sphere.ppm")