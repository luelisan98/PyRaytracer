import pytest

from rayTracer.plane import Plane
from rayTracer.rays import Rays
from rayTracer.tuples import Tuples
from rayTracer.intersection import Intersection

def test_constant_normal():
	p = Plane()
	n1 = p.local_normal_at(Tuples().Point(0, 0, 0))
	n2 = p.local_normal_at(Tuples().Point(10, 0, -10))
	n3 = p.local_normal_at(Tuples().Point(-5, 0, 150))
	assert n1 == Tuples().Vector(0, 1, 0)
	assert n2 == Tuples().Vector(0, 1, 0)
	assert n3 == Tuples().Vector(0, 1, 0)

def test_ray_parallel():
	p = Plane()
	r = Rays(Tuples().Point(0, 10, 0), Tuples().Vector(0, 0, 1))
	xs = p.intersect(r)
	assert len(xs) == 0

def test_ray_coplanar():
	p = Plane()
	r = Rays(Tuples().Point(0, 0, 0), Tuples().Vector(0, 0, 1))
	xs = p.intersect(r)
	assert len(xs) == 0

def test_ray_above():
	p = Plane()
	r = Rays(Tuples().Point(0, 1, 0), Tuples().Vector(0, -1, 0))
	xs = p.intersect(r)
	assert len(xs) == 1
	assert xs[0].t == 1
	assert xs[0].obj == p

def test_ray_below():
	p = Plane()
	r = Rays(Tuples().Point(0, -1, 0), Tuples().Vector(0, 1, 0))
	xs = p.intersect(r)

	assert len(xs) == 1
	assert xs[0].t == 1
	assert xs[0].obj == p