from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from rayTracer.worlds import World
from rayTracer.sphere import Sphere
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.camera import Camera
from rayTracer.plane import Plane
import math

def main():
	
	floor = Plane()
	floor.transform = Transformations().translation(0,0,0)
	floor.material = Materials()
	floor.material.color = Colors(1,0.9,0.9)
	
	middle = Sphere()
	middle.transform = Transformations().translation(-0.5, 1, 0.5)
	middle.material = Materials()
	middle.material.color = Colors(0.1, 1, 0.5)
	middle.material.diffuse = 0.7
	middle.material.specular = 0.3

	right = Sphere()
	right.transform = Transformations().translation(1.5, 0.5, -0.5) * Transformations().scaling(0.5, 0.5, 0.5)
	right.material = Materials()
	right.material.color = Colors(0.5, 1, 0.1)
	right.material.diffuse = 0.7
	right.material.specular = 0.3

	left = Sphere()
	left.transform = Transformations().translation(-1.5, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33)
	left.material = Materials()
	left.material.color = Colors(1, 0.8, 0.1)
	left.material.diffuse = 0.7
	left.material.specular = 0.3

	world = World()
	world.light.point_light(Tuples().Point(-10, 10, -10),
							Colors(1, 1, 1))
	
	world.objects.append(floor)
	world.objects.append(middle) 
	world.objects.append(left)
	world.objects.append(right)
	
	camera = Camera(300, 150, math.pi/3)
	camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5),
														Tuples().Point(0, 1, 0),
														Tuples().Vector(0, 1, 0))
	
	
	
	canvas = camera.render(world)
	canvas.canvas_to_ppm("cap9.ppm")
	
   
if __name__ == "__main__":
	main()