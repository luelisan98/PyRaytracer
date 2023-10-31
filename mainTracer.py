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
	
	material_blue = Materials()
	material_blue.color = Colors(0.137255, 0.419608, 0.556863)
	material_blue.ambient = 0.2
	material_blue.specular = 0.3
	material_blue.diffuse = 0.8
	material_blue.shininess = 200

	material_green = Materials()
	material_green.color = Colors(0.18431, 0.309804, 0.184314)
	material_green.ambient = 0.2
	material_green.specular = 0.3
	material_green.diffuse = 0.8
	material_green.shininess = 200


	base = Sphere()
	base.transform = Transformations().translation(0, 0, 0)
	base.material = material_blue

	head = Sphere()
	head.transform = Transformations().translation(0, 1.5, 0) * Transformations().scaling(0.5,0.5,0.5)
	head.material = material_blue

	arm1 = Sphere()
	arm1.transform = Transformations().translation(-0.5, 0, 0) * Transformations().scaling(-0.35,1,1) * Transformations().rotation_z(0.4)
	arm1.material = material_blue

	arm2 = Sphere()
	arm2.transform = Transformations().translation(0.5, 0, 0) * Transformations().scaling(-0.35,1,1) * Transformations().rotation_z(-0.4)
	arm2.material = material_blue 

	
	
	world.objects.append(floor)
	world.objects.append(left_wall) 
	world.objects.append(right_wall)
	
	world.objects.append(base)
	world.objects.append(head)
	world.objects.append(arm1)
	world.objects.append(arm2)

	
	camera = Camera(150, 75, math.pi/3)
	camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5),
														Tuples().Point(0, 1, 0),
														Tuples().Vector(0, 1, 0))
	canvas = camera.render(world)
	canvas.canvas_to_ppm("purpleCircle2.ppm")
	
   
if __name__ == "__main__":
	main()