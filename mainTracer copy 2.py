import math

from rayTracer.camera import Camera
from rayTracer.lights import Lights
from rayTracer.transformations import Transformations
from rayTracer.pattern import Checker, Ring, Gradient, Stripe
from rayTracer.sphere import Sphere 
from rayTracer.plane import Plane
from rayTracer.tuples import Tuples
from rayTracer.worlds import World
from rayTracer.colors import Colors

if __name__ == "__main__":
    world = World()

    floor = Plane()
    floor.material.specular = 0
    floor.material.pattern = Checker(Colors(1, 0.9, 0.9), Colors(0, 0.1, 0.1))
    floor.material.reflective = 0.5
    world.objects.append(floor)

    middle = Sphere().glass_sphere()
    middle.set_transform(Transformations().translation(-0.5, 1, 0.5))
    middle.material.pattern = Ring(Colors(0.1, 1, 0.5), Colors(0.9, 0, 0.5))
    middle.material.pattern.transform = Transformations().scaling(0.1, 0.1, 0.1)
    middle.material.reflective = 1
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    world.objects.append(middle)

    right = Sphere()
    right.set_transform(Transformations().translation(1.5, 0.5, -0.5) * Transformations().scaling(0.5, 0.5, 0.5))
    right.material.pattern = Gradient(Colors(0.5, 1, 0.1), Colors(0.5, 0, 0.9))
    right.material.pattern.transform = Transformations().scaling(0.5, 0.5, 0.5)
    right.material.transparency = 0.5
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    right.material.reflective = 0.5
    right.material.refractive_index = 2
    world.objects.append(right)

    left = Sphere()
    left.set_transform(Transformations().translation(-1.5, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33))
    left.material.pattern = Stripe(Colors(1, 0.8, 0.1), Colors(0, 0.2, 0.9))
    left.material.pattern.transform = Transformations().scaling(0.1, 0.1, 0.1)
    left.material.transparency = 0
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    left.material.reflective = 1
    left.material.refractive_index = 0.5
    world.objects.append(left)

    world.light = Lights()
    world.light.point_light(Tuples().Point(-10, 10, -10), Colors(1, 1, 1))
    camera = Camera(800, 400, math.pi / 3)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5), Tuples().Point(0, 1, 0), Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)

    with open("../images/reflection.ppm", "w") as ppm_file:
        ppm_file.write(canvas.to_ppm())