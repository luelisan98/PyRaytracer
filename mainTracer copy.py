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

    # Floor
    floor = Plane()
    floor.material.color = Colors(1, 0.9, 0.9)
    floor.material.specular = 0
    world.objects.append(floor)

    # Ceiling
    ceiling = Plane()
    ceiling.set_transform(Transformations().translation(0, 5, 0))
    ceiling.material.color = Colors(1, 0.9, 0.9)
    ceiling.material.specular = 0
    world.objects.append(ceiling)

    # Back wall
    back_wall = Plane()
    back_wall.set_transform(Transformations().translation(0, 0, 5) * Transformations().rotation_x(math.pi / 2))
    back_wall.material.color = Colors(1, 0.9, 0.9)
    back_wall.material.specular = 0
    world.objects.append(back_wall)

    middle = Sphere()
    middle.set_transform(Transformations().translation(-0.5, 1, 0.5))
    middle.material.color = Colors(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    world.objects.append(middle)

    right = Sphere()
    right.set_transform(Transformations().translation(1.5, 0.5, -0.5) * Transformations().scaling(0.5, 0.5, 0.5))
    right.material.color = Colors(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    world.objects.append(right)

    left = Sphere()
    left.set_transform(Transformations().translation(-1.5, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33))
    left.material.color = Colors(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    world.objects.append(left)

    world.light = Lights()
    world.light.point_light(Tuples().Point(-10, 10, -10), Colors(1, 1, 1))
    camera = Camera(300, 150, math.pi / 3)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 3, -5), Tuples().Point(0, 1, 0),
                                                        Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)

    canvas.canvas_to_ppm("room.ppm")
