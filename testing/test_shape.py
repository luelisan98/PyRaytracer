import pytest
from rayTracer.shapes import Shape
from rayTracer.matrix import Matrix
from rayTracer.transformations import Transformations
from rayTracer.materials import Materials
from rayTracer.tuples import Tuples
from rayTracer.matrix import Matrix
from rayTracer.rays import Rays
from rayTracer.intersection import Intersection


def test_default_transformation():
    s = Shape().test_shape()
    identity = Matrix(4,4).identity()
    assert s.transform == identity

def test_set_transform():
    s = Shape().test_shape()
    t = Transformations().translation(2,3,4)
    s.set_transform(t)
    assert s.transform == Transformations().translation(2,3,4)

def test_default_material():
    s = Shape().test_shape()
    assert s.material == Materials()

def test_assigning_material():
    s = Shape().test_shape()
    m = Materials()
    m.ambient = 1
    s.material = m
    assert s.material == m

def test_intersecting_scaled_shape():
    r = Rays(Tuples().Point(0,0,-5), Tuples().Vector(0,0,1))
    s = Shape().test_shape()
    s.set_transform(Transformations().scaling(2,2,2))
    xs = Intersection().intersect(s,r)
    s.intersect(r)
    assert s.saved_ray.origin == Tuples().Point(0,0,-2.5)
    assert s.saved_ray.direction == Tuples().Vector(0,0,0.5)
    assert len(xs) == 2
    assert xs[0].t == 3
    assert xs[1].t == 7

def test_intersecting_translated_shape():
    r = Rays(Tuples().Point(0,0,-5), Tuples().Vector(0,0,1))
    s = Shape().test_shape()
    s.set_transform(Transformations().translation(5,0,0))
    xs = Intersection().intersect(s,r)
    s.intersect(r)
    assert s.saved_ray.origin == Tuples().Point(-5,0,-5)
    assert s.saved_ray.direction == Tuples().Vector(0,0,1)
    assert len(xs) == 0

def test_normal_translated_sphere():
    trans = Transformations()
    s = Shape().test_shape()
    s.set_transform(trans.translation(0,1,0))
    Point = Tuples().Point(0, 1.70711, -0.70711)
    expected = Tuples().Vector(0, 0.70711, -0.70711)
    normal = s.normal_at(Point)
    assert normal == expected

def test_normal_transformed_sphere():
    trans = Transformations()
    s = Shape().test_shape()
    m = trans.scaling(1, 0.5, 1) * trans.rotation_z(3.14159/5)
    s.set_transform(m)
    Point = Tuples().Point(0, (2 ** 0.5) / 2, -(2 ** 0.5) / 2)
    expected = Tuples().Vector(0, 0.97014, -0.24254)
    normal = s.normal_at(Point)
    assert normal == expected

