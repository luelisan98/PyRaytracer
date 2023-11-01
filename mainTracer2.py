from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from rayTracer.worlds import World
from rayTracer.sphere import Sphere
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.camera import Camera
import math

def main():
	
	world = World()
	
	world.light.point_light(Tuples().Point(-10, 10, -10),
							Colors(1, 1, 1))
	
	floor = Sphere()
	floor.transform = Transformations().scaling(10, 0.01, 10)
	floor.material = Materials()
	floor.material.color = Colors(1, 0.9, 0.9)
	floor.material.specular = 0
	
	left_wall = Sphere()
	left_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(-math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
	left_wall.material = floor.material
	
	right_wall = Sphere()
	right_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
	right_wall.material = floor.material
	
	material_yellow = Materials()
	material_yellow.color = Colors(0.858824, 0.858824, 0.439216)

	material_white = Materials()
	material_white.color = Colors(1, 1, 1)

	scale = Transformations().scaling(0.13,0.5,0.5)

	base = Sphere()
	base.transform = Transformations().scaling(0.5,0.5,0.5) *  Transformations().translation(0, 1.5, 0)
	base.material = material_yellow

	petal1 = Sphere()
	petal1.transform = scale * Transformations.translation(0,3,0)
	petal1.material = material_white

	petal2 = Sphere()
	petal2.transform = scale * Transformations.translation(0,0.5,0)
	petal2.material = material_white

	petal3 = Sphere()
	petal3.transform = Transformations.rotation_z(math.pi/2) * scale * Transformations.translation(6,1,0)
	petal3.material = material_white

	petal4 = Sphere()
	petal4.transform = Transformations.rotation_z(math.pi/2) * scale * Transformations.translation(6,-1,0)
	petal4.material = material_white

	petal5 = Sphere()
	petal5.transform = Transformations.rotation_z(math.pi/4) * scale * Transformations.translation(4,2.5,0)
	petal5.material = material_white

	world.objects.append(floor)
	world.objects.append(left_wall) 
	world.objects.append(right_wall)
	
	world.objects.append(base)
	world.objects.append(petal1)
	world.objects.append(petal2)
	world.objects.append(petal3)
	world.objects.append(petal4)
	world.objects.append(petal5)
	
	camera = Camera(int(900), int(500), math.pi/3)
	camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5),
														Tuples().Point(0, 1, 0),
														Tuples().Vector(0, 1, 0))
	canvas = camera.render(world)
	canvas.canvas_to_ppm("escena2.ppm")
	
   
if __name__ == "__main__":
	main()