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

if __name__ == "__main__":
    world = World()

    floor = Plane()
    floor.material.specular = 0
    #floor.material.pattern = Checker(Colors(1, 0.9, 0.9), Colors(0, 0.1, 0.1))
    floor.material.reflective = 0.5
    world.objects.append(floor)

    middle = Sphere()
    middle.set_transform(Transformations().translation(-0.25, 1, 0.5))
    middle.material.pattern = Ring(Colors(0.1, 1, 0.5), Colors(0.9, 0, 0.5))
    middle.material.pattern.transform = Transformations().scaling(0.1, 0.1, 0.1)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    world.objects.append(middle)

    right = Sphere()
    right.set_transform(Transformations().translation(-1.25, 0.5, -0.5) * Transformations().scaling(0.33, 0.33, 0.33))
    right.material.pattern = Gradient(Colors(0.5, 1, 0.1), Colors(0.5, 0, 0.9))
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    world.objects.append(right)

    left = Sphere()
    left.set_transform(Transformations().translation(-2, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33))
    left.material.pattern = Stripe(Colors(1, 0.8, 0.1), Colors(0, 0.2, 0.9))
    left.material.pattern.transform = Transformations().scaling(0.1,0.1,0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    world.objects.append(left)

    # Add a new sphere
    new_sphere = Sphere()
    new_sphere.set_transform(Transformations().translation(1, 1, -1.5) * Transformations().scaling(0.5, 0.5, 0.5))
    new_sphere.material.pattern = Checker(Colors(0.1, 0.1, 1), Colors(0.9, 0.9, 0))
    new_sphere.material.pattern.transform = Transformations().rotation_x(60)
    new_sphere.material.diffuse = 0.7
    new_sphere.material.specular = 0.3
    world.objects.append(new_sphere)

    world.light = Lights()
    world.light.point_light(Tuples().Point(-10, 10, -10), Colors(1, 1, 1))
    camera = Camera(300*4, 150*4, math.pi / 2.5)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5), Tuples().Point(0, 1, 0), Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)
    canvas.canvas_to_ppm("pattern.ppm")
