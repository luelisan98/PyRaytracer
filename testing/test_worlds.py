import pytest
from rayTracer.worlds import World
from rayTracer.rays import Rays
from rayTracer.sphere import Sphere
from rayTracer.intersection import Intersection
from rayTracer.computations import Computations
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.plane import Plane
from rayTracer.pattern import Pattern


import math

def test_creating_world():
	world = World()
	assert len(world.objects) == 0

def test_creating_default_world():
	world = World()
	world.default_world()

	light = Lights()
	point = Tuples().Point(-10, 10, -10)
	color = Colors(1, 1, 1)
	light.point_light(point, color)

	material = Materials()
	material_color = Colors(0.8, 1.0, 0.6)
	material.color = material_color
	material.diffuse = 0.7
	material.specular = 0.2

	s1 = Sphere()
	s1.material = material

	trans = Transformations()
	s2 = Sphere()
	s2.set_transform(trans.scaling(0.5, 0.5, 0.5))

	assert world.light == light
	assert s1 in world.objects
	assert s2 in world.objects

def test_intersect_world_ray():
	world = World()
	world.default_world()

	origin = Tuples().Point(0, 0, -5)
	direction = Tuples().Vector(0, 0, 1)
	ray = Rays(origin, direction)

	inter = Intersection()
	xs = inter.intersect_world(world, ray)

	assert len(xs) == 4
	assert xs[0].t == 4
	assert xs[1].t == 4.5
	assert xs[2].t == 5.5
	assert xs[3].t == 6

def test_shading_intersection():
	world = World()
	world.default_world()

	origin = Tuples().Point(0, 0, -5)
	direction = Tuples().Vector(0, 0, 1)
	ray = Rays(origin, direction)

	shape = world.objects[0]

	i = Intersection(4, shape)
	com = Computations()
	comps = com.prepare_computations(i, ray)
	c = com.shade_hit(world, comps)
	col = Colors(0.38066, 0.47583, 0.2855)
	assert c == col

def test_shading_intersection_inside():
	world = World()
	world.default_world()

	l = Lights()
	point = Tuples().Point(0, 0.25, 0)
	color = Colors(1, 1, 1)
	l.point_light(point, color)
	world.light = l

	origin = Tuples().Point(0, 0, 0)
	direction = Tuples().Vector(0, 0, 1)
	ray = Rays(origin, direction)

	shape = world.objects[1]

	i = Intersection(0.5, shape)
	com = Computations()
	comps = com.prepare_computations(i, ray)
	c = com.shade_hit(world, comps)
	col = Colors(0.90498, 0.90498, 0.90498)

	assert c == col

def test_color_ray_misses():
	world = World()
	world.default_world()

	origin = Tuples().Point(0, 0, -5)
	direction = Tuples().Vector(0, 1, 0)
	ray = Rays(origin, direction)

	com = Computations()
	c = com.color_at(world, ray)
	col = Colors(0, 0, 0)

	assert c == col

def test_color_ray_hits():
	world = World()
	world.default_world()

	origin = Tuples().Point(0, 0, -5)
	direction = Tuples().Vector(0, 0, 1)
	ray = Rays(origin, direction)

	com = Computations()
	c = com.color_at(world, ray)
	col = Colors(0.38066, 0.47583, 0.2855)

	assert c == col

def test_color_intersection_behind_ray():
	world = World()
	world.default_world()

	outer = world.objects[0]
	outer.material.ambient = 1

	inner = world.objects[1]
	inner.material.ambient = 1

	origin = Tuples().Point(0, 0, 0.75)
	direction = Tuples().Vector(0, 0, -1)
	ray = Rays(origin, direction)

	com = Computations()
	c = com.color_at(world, ray)

	assert c == inner.material.color
	   
def test_no_shadow_nothing_collinear_with_point_light():
	world = World().default_world()
	p = Tuples().Point(0, 10, 0)
	assert not world.is_shadowed(p)
	
def test_shadow_with_object_between_point_light():
	world = World().default_world()
	p = Tuples().Point(10, -10, 10)
	assert world.is_shadowed(p)
	
def test_no_shadow_with_object_behind_light():
	world = World().default_world()
	p = Tuples().Point(-20, 20, -20)
	assert not world.is_shadowed(p)
	
def test_no_shadow_with_object_behind_point():
	world = World().default_world()
	p = Tuples().Point(-2, 2, -2)
	assert not world.is_shadowed(p)
	
def test_shade_hit_given_intersection_in_shadow():
	w = World()
	l = Lights()
	l.point_light(Tuples().Point(0, 0, -10), Colors(1, 1, 1))
	w.light = l
	s1 = Sphere()
	w.objects.append(s1)
	s2 = Sphere()
	s2.transform = Transformations.translation(0, 0, 10)
	w.objects.append(s2)
	r = Rays(Tuples().Point(0, 0, 5), Tuples().Vector(0, 0, 1))
	i = Intersection(4, s2)
	comps = Computations().prepare_computations(i, r)
	c = comps.shade_hit(w,comps)
	assert c == Colors(0.1, 0.1, 0.1)
	
def test_reflected_color_nonreflective_material():
	w = World().default_world()
	r = Rays(Tuples().Point(0,0,0), Tuples().Vector(0,0,1))
	shape = w.objects[1]
	shape.material.ambient = 1 
	i = Intersection(1, shape)
	comps = Computations().prepare_computations(i,r)
	color = Computations().reflected_color(w,comps)
	assert color == Colors(0,0,0)
	
def test_reflected_reflective_material():
	w = World().default_world()
	shape = Plane()
	shape.material.reflective = 0.5
	shape.set_transform(Transformations().translation(0, -1, 0))
	w.objects.append(shape)
	r = Rays(Tuples().Point(0, 0, -3), Tuples().Vector(0, -math.sqrt(2) / 2, math.sqrt(2) / 2))
	i = Intersection(math.sqrt(2), shape)
	comps = Computations().prepare_computations(i,r)
	color = Computations().reflected_color(w,comps)
	assert color == Colors(0.19032, 0.2379, 0.14274)
	
def test_shade_hit():
	w = World().default_world()
	shape = Plane()
	shape.material.reflective = 0.5
	shape.set_transform(Transformations().translation(0, -1, 0))
	w.objects.append(shape)
	r = Rays(Tuples().Point(0, 0, -3), Tuples().Vector(0, -math.sqrt(2) / 2, math.sqrt(2) / 2))
	i = Intersection(math.sqrt(2), shape)
	comps = Computations().prepare_computations(i,r)
	color = Computations().shade_hit(w, comps)
	assert color == Colors(0.87677, 0.92436, 0.82918)
	
def test_mutually_reflective():
	w = World()
	point = Tuples().Point(0,0,0)
	color = Colors(1, 1, 1)
	w.light.point_light(point, color)

	lower = Plane()
	lower.material.reflective = 1
	lower.set_transform(Transformations().translation(0,-1,0))
	w.objects.append(lower)

	upper = Plane()
	upper.material.reflective = 1
	upper.set_transform(Transformations().translation(0,1,0))
	w.objects.append(upper)

	r = Rays(Tuples().Point(0,0,0), Tuples().Vector(0,1,0))
	Computations().color_at(w,r)

def test_reflection_maximum_recursion():
    w = World()
    shape = Plane()
    shape.material.reflective = 0.5
    shape.set_transform(Transformations().translation(0, -1, 0))
    w.objects.append(shape)
    r = Rays(Tuples().Point(0, 0, -3), Tuples().Vector(0, -math.sqrt(2) / 2, math.sqrt(2) / 2))
    i = Intersection(math.sqrt(2), shape)
    comps = Computations().prepare_computations(i,r)
    color = Computations().reflected_color(w,comps)
    assert color == Colors(0, 0, 0)

def test_refraction_color_opaque_surface():
	w = World().default_world()
	shape = w.objects[0]
	r = Rays(Tuples().Point(0,0,-5), Tuples().Vector(0,0,1))
	xs = Intersection().intersections(Intersection(4,shape), Intersection(6,shape))
	comps = Computations().prepare_computations(xs[0],r,xs)
	color = Computations().refracted_color(w,comps)
	assert color == Colors(0,0,0)

def test_refraction_maximum_depth():
	w = World().default_world()
	shape = w.objects[0]
	shape.material.transparency = 1
	shape.material.refractive_index = 1.5
	xs = Intersection().intersections(Intersection(4, shape), Intersection(6, shape))
	comps = Computations().prepare_computations(xs[0],Rays(Tuples().Point(0, 0, -5), Tuples().Vector(0, 0, 1)), xs)
	color = comps.refracted_color(w,comps)
	assert color == Colors(0,0,0)

def test_refract_color_total_internal_reflection():
	w = World().default_world()
	shape = w.objects[0]
	shape.material.transparency = 1
	shape.material.refractive_index = 1.5
	r = Rays(Tuples().Point(0,0,math.sqrt(2)/2), Tuples().Vector(0,1,0))
	xs = Intersection().intersections(Intersection(-math.sqrt(2)/2,shape),Intersection(math.sqrt(2)/2, shape))
	comps = Computations().prepare_computations(xs[1], r, xs)
	c = Computations().refracted_color(w,comps,5)
	assert c == Colors(0,0,0)

def test_refracted_color_refracted_ray():
	w = World().default_world()
	a = w.objects[0]
	a.material.ambient = 1 
	a.material.pattern = Pattern().test_pattern()
	b = w.objects[1]
	b.material.transparency = 1
	b.material.refractive_index = 1.5
	r = Rays(Tuples().Point(0,0,0.1), Tuples().Vector(0,1,0))
	xs = Intersection().intersections(Intersection(-0.9899, a), Intersection(-0.4899, b), Intersection(0.4899, b), Intersection(0.9899,a))
	comps = Computations().prepare_computations(xs[2], r, xs)
	c = Computations().refracted_color(w,comps,5)
	assert c == Colors(0,0.99888,0.04725)
	
def test_shade_hit_transparent():
	w = World().default_world()
	floor = Plane()
	floor.set_transform(Transformations().translation(0,-1,0))
	floor.material.transparency = 0.5
	floor.material.refractive_index = 1.5
	w.objects.append(floor)

	ball = Sphere()
	ball.material.color = Colors(1,0,0)
	ball.material.ambient = 0.5
	ball.set_transform(Transformations().translation(0,-3.5,-0.5))
	w.objects.append(ball)

	r = Rays(Tuples().Point(0,0,-3), Tuples().Vector(0,-math.sqrt(2)/2,math.sqrt(2)/2))
	xs = Intersection().intersections(Intersection(math.sqrt(2), floor))
	comps = Computations().prepare_computations(xs[0],r,xs)
	color = Computations().shade_hit(w,comps,5)
	assert color == Colors(0.93642, 0.68642, 0.68642)

def test_shade_hit_reflective_transparent_material():
	w = World().default_world()
	r = Rays(Tuples().Point(0,0,-3), Tuples().Vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
	floor = Plane()
	floor.set_transform(Transformations().translation(0,-1,0))
	floor.material.reflective = 0.5
	floor.material.transparency = 0.5
	floor.material.refractive_index = 1.5
	w.objects.append(floor)

	ball = Sphere()
	ball.material.color = Colors(1,0,0)
	ball.material.ambient = 0.5
	ball.set_transform(Transformations().translation(0,-3.5,-0.5))
	w.objects.append(ball)

	xs = Intersection().intersections(Intersection(math.sqrt(2), floor))
	comps = Computations().prepare_computations(xs[0], r, xs)
	color = Computations().shade_hit(w,comps,5)
	assert color == Colors(0.93391,0.69643, 0.69243)
