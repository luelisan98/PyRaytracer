from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from rayTracer.worlds import World
from rayTracer.sphere import Sphere
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.camera import Camera
from rayTracer.plane import Plane
from rayTracer.pattern import Checker, Gradient, Stripe, Ring
from rayTracer.lights import Lights
import math

sapphire_material = Materials()
sapphire_material.color = Colors(0.05, 0.2, 0.4)  # Deep blue color for sapphire
sapphire_material.ambient = 0.2
sapphire_material.diffuse = 0.5
sapphire_material.specular = 0.8
sapphire_material.shininess = 100.0
sapphire_material.reflective = 0.2
sapphire_material.transparency = 0.8
sapphire_material.refractive_index = 1.77  # Typical refractive index for sapphire

fused_quarz_material = Materials()
fused_quarz_material.color = Colors(1,1,1)
fused_quarz_material.ambient = 0.1
fused_quarz_material.diffuse = 0.6 
fused_quarz_material.specular = 0.8
fused_quarz_material.shininess = 150.0 
fused_quarz_material.reflective = 0.2
fused_quarz_material.transparency = 0.9 
fused_quarz_material.refractive_index = 1.46

diamond = Materials()
diamond.color = Colors(1.0, 1.0, 1.0)  # Colorless, so use white
diamond.ambient = 0.1
diamond.diffuse = 0.2
diamond.specular = 0.8
diamond.shininess = 200.0
diamond.reflective = 0.5  # Diamonds have high reflectivity
diamond.transparency = 0.9  # Diamonds are highly transparent
diamond.refractive_index = 2.42  # Refractive index of diamond

fluorite = Materials()
fluorite.color = Colors(0.8, 1.0, 0.8)
fluorite.shininess=30.0
fluorite.transparency=0.8
fluorite.refractive_index=1.43
fluorite.ambient = 0.1
fluorite.diffuse = 0.6
fluorite.specular = 0.5
fluorite.reflective = 0.1

steel = Materials()

steel.color = Colors(0.7, 0.7, 0.7)  # A typical silver-gray color for steel
steel.ambient = 0.1
steel.diffuse = 0.6  # Some diffuse reflection for metals
steel.specular = 0.3  # Moderate specular reflection for steel
steel.shininess = 30.0  # Moderate shininess for a balanced specular highlight
steel.reflective = 0.6  # Reflective component for metal
steel.transparency = 0.0  # Metals are generally not transparent
steel.refractive_index = 1.0  # No refraction for metals



if __name__ == "__main__":
    world = World()

    floor = Plane()
    floor.material.specular = 0 
    floor.material.reflective = 0.5
    world.objects.append(floor)

    middle = Sphere()
    middle.set_transform(Transformations().translation(-0.25, 1, 0.5))
    middle.material = fused_quarz_material
    world.objects.append(middle)

    right = Sphere()
    right.set_transform(Transformations().translation(-1.25, 0.5, -0.5) * Transformations().scaling(0.33, 0.33, 0.33))
    right.material = sapphire_material
    world.objects.append(right)

    left = Sphere()
    left.set_transform(Transformations().translation(-2, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33))
    left.material = steel
    world.objects.append(left)

    # Add a new sphere
    new_sphere = Sphere()
    new_sphere.set_transform(Transformations().translation(1, 1, -1.5) * Transformations().scaling(0.5, 0.5, 0.5))
    new_sphere.material = fluorite
    world.objects.append(new_sphere)

    world.light = Lights()
    world.light.point_light(Tuples().Point(-10, 10, -10), Colors(1, 1, 1))
    camera = Camera(300*4, 150*4, math.pi / 2.5)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5), Tuples().Point(0, 1, 0), Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)
    canvas.canvas_to_ppm("reflection.ppm")
