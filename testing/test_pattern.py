from rayTracer.colors import Colors
from rayTracer.pattern import Stripe
from rayTracer.tuples import Tuples
from rayTracer.sphere import Sphere
from rayTracer.transformations import Transformations


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
	obj.transform = Transformations().scaling(2,2,2)
	pattern = Stripe(white,black)
	c = pattern.pattern_at_shape(obj, Tuples().Point(1.5,0,0))
	assert c == white

def test_pattern_pattern_transform():
	obj = Sphere()
	pattern = Stripe(white,black)
	pattern.transform = Transformations().scaling(2,2,2)
	c = pattern.pattern_at_shape(obj, Tuples().Point(1.5,0,0))
	assert c == white

def test_pattern_obj_pattern_transform():
	obj = Sphere()
	obj.transform = Transformations().scaling(2,2,2)
	pattern = Stripe(white,black)
	pattern.transform = Transformations().translation(0.5,0,0)
	c = pattern.pattern_at_shape(obj, Tuples().Point(2.5,0,0))
	assert c == white