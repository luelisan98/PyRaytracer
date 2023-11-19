from rayTracer.colors import Colors
from rayTracer.pattern import Pattern
from rayTracer.tuples import Tuples


import pytest 


@pytest.fixture
def white():
	return Colors(1,1,1)

@pytest.fixture
def black():
	return Colors(0,0,0)

def test_stripe_pattern():

	pattern = Pattern().stripe_pattern(white, black)

	assert pattern.a == white
	assert pattern.b == black

def test_pattern_at_y():
	pattern = Pattern().stripe_pattern(white, black)
	assert pattern.stripe_at( Tuples().Point(0,0,0) ) == white
	assert pattern.stripe_at( Tuples().Point(0,1,0) ) == white
	assert pattern.stripe_at( Tuples().Point(0,2,0) ) == white

def test_pattern_at_z():
	pattern = Pattern().stripe_pattern(white, black)
	assert pattern.stripe_at( Tuples().Point(0,0,0) ) == white
	assert pattern.stripe_at( Tuples().Point(0,0,1) ) == white
	assert pattern.stripe_at( Tuples().Point(0,0,2) ) == white

def test_pattern_at_x():
	pattern = Pattern().stripe_pattern(white, black)
	assert pattern.stripe_at(Tuples().Point(0, 0, 0)) == white
	assert pattern.stripe_at(Tuples().Point(0.9, 0, 1)) == white
	assert pattern.stripe_at(Tuples().Point(1, 0, 0)) == black
	assert pattern.stripe_at(Tuples().Point(-0.1, 0, 0)) == black
	assert pattern.stripe_at(Tuples().Point(-1, 0, 0)) == black
	assert pattern.stripe_at(Tuples().Point(-1.1, 0, 0)) == white
	
