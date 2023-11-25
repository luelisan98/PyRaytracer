from rayTracer.colors import Colors
from rayTracer.pattern import Stripe,Pattern,Gradient,Ring,Checker
from rayTracer.tuples import Tuples
from rayTracer.sphere import Sphere
from rayTracer.transformations import Transformations
from rayTracer.matrix import Matrix

import pytest 


@pytest.fixture
def white():
	return Colors(1,1,1)

@pytest.fixture
def black():
	return Colors(0,0,0)

def test_stripe_pattern():
	pattern = Stripe(white, black)
	assert pattern.a == white
	assert pattern.b == black

def test_default_pattern():
	pattern = Pattern().test_pattern()
	assert pattern.transform == Matrix(4,4).identity()

def test_pattern_transform():
	pattern = Pattern().test_pattern()
	pattern.set_pattern_transform(Transformations().translation(1,2,3))
	assert pattern.transform == Transformations().translation(1,2,3)


def test_pattern_at_y():
	pattern = Stripe(white, black)
	assert pattern.pattern_at( Tuples().Point(0,0,0) ) == white
	assert pattern.pattern_at( Tuples().Point(0,1,0) ) == white
	assert pattern.pattern_at( Tuples().Point(0,2,0) ) == white

def test_pattern_at_z():
	pattern = Stripe(white, black)
	assert pattern.pattern_at( Tuples().Point(0,0,0) ) == white
	assert pattern.pattern_at( Tuples().Point(0,0,1) ) == white
	assert pattern.pattern_at( Tuples().Point(0,0,2) ) == white

def test_pattern_at_x():
	pattern = Stripe(white, black)
	assert pattern.pattern_at(Tuples().Point(0, 0, 0)) == white
	assert pattern.pattern_at(Tuples().Point(0.9, 0, 1)) == white
	assert pattern.pattern_at(Tuples().Point(1, 0, 0)) == black
	assert pattern.pattern_at(Tuples().Point(-0.1, 0, 0)) == black
	assert pattern.pattern_at(Tuples().Point(-1, 0, 0)) == black
	assert pattern.pattern_at(Tuples().Point(-1.1, 0, 0)) == white
	
def test_pattern_obj_transform():
	obj = Sphere()
	obj.set_transform(Transformations().scaling(2,2,2))
	pattern = Stripe(white,black)
	c = pattern.pattern_at_shape(obj, Tuples().Point(1.5,0,0))
	assert c == white

def test_pattern_pattern_transform():
	obj = Sphere()
	pattern = Stripe(white,black)
	pattern.set_pattern_transform(Transformations().scaling(2,2,2))
	c = pattern.pattern_at_shape(obj, Tuples().Point(1.5,0,0))
	assert c == white

def test_pattern_obj_pattern_transform():
	obj = Sphere()
	obj.set_transform( Transformations().scaling(2,2,2))
	pattern = Stripe(white,black)
	pattern.set_pattern_transform(Transformations().translation(0.5,0,0))
	c = pattern.pattern_at_shape(obj, Tuples().Point(2.5,0,0))
	assert c == white

def test_gradient():
	pattern = Gradient(Colors(1,1,1), Colors(0,0,0))
	assert pattern.pattern_at(Tuples().Point(0,0,0)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(0.25,0,0)) == Colors(0.75,0.75,0.75)
	assert pattern.pattern_at(Tuples().Point(0.5,0,0)) == Colors(0.5,0.5,0.5)
	assert pattern.pattern_at(Tuples().Point(0.75,0,0)) == Colors(0.25,0.25,0.25)

def test_ring():
	pattern = Ring(Colors(1,1,1), Colors(0,0,0))
	assert pattern.pattern_at(Tuples().Point(0,0,0)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(1,0,0)) == Colors(0,0,0)
	assert pattern.pattern_at(Tuples().Point(0,0,1)) == Colors(0,0,0)
	assert pattern.pattern_at(Tuples().Point(0.708,0,0.708)) == Colors(0,0,0)
	
def test_checker_repeat_x():
	pattern = Checker(Colors(1,1,1), Colors(0,0,0))
	assert pattern.pattern_at(Tuples().Point(0, 0, 0)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(0.99, 0, 0)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(1.01, 0, 0)) == Colors(0,0,0)

def test_checker_repeat_y():
	pattern = Checker(Colors(1,1,1), Colors(0,0,0))
	assert pattern.pattern_at(Tuples().Point(0, 0, 0)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(0, 0.99, 0)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(0, 1.01, 0)) == Colors(0,0,0)

def test_checker_repeat_z():
	pattern = Checker(Colors(1,1,1), Colors(0,0,0))
	assert pattern.pattern_at(Tuples().Point(0, 0, 0)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(0, 0, 0.99)) == Colors(1,1,1)
	assert pattern.pattern_at(Tuples().Point(0, 0, 1.01)) == Colors(0,0,0)