from math import sqrt
import pytest

from rayTracer.tuples import Tuples


def test_tuples_1(): 
    t1 = Tuples()
    t2 = Tuples()
    t1.Point(4.3, -4.2, 3.1)
    t2.Vector(4.3, -4.2, 3.1)
    assert True == t1.isPoint()
    assert True == t2.isVector()
    
def test_tuples_2(): 
    t1 = Tuples()
    t2 = Tuples()
    t1.Point(4.3, -4.2, 3.1)
    t2.Vector(4.3, -4.2, 3.1)
    assert False == t1.isVector()
    assert False == t2.isPoint()

def test_tuples_add(): 
    t1 = Tuples()
    t2 = Tuples()
    expected = Tuples()
    expected.Point(1,1,6)
    t1.Point(3, -2, 5)
    t2.Vector(-2, 3, 1)
    assert True == ( expected == t1 + t2 )

def test_tuples_subtract(): 
    t1 = Tuples()
    t2 = Tuples()
    expected = Tuples()
    expected.Vector(-2, -4, -6)
    t1.Point(3, 2, 1)
    t2.Point(5, 6, 7)
    assert True == ( expected == (t1 - t2))

def test_tuples_subtract_vector_point():
    t1 = Tuples()
    t2 = Tuples()
    expected = Tuples()
    t1.Point(3, 2, 1)
    t2.Vector(5, 6, 7)
    expected.Point(-2, -4, -6)
    assert True == ( expected == (t1 - t2))
    
def test_tuples_subtract_vectors():
    t1 = Tuples()
    t2 = Tuples()
    expected = Tuples()
    t1.Vector(3, 2, 1)
    t2.Vector(5, 6, 7)
    expected.Vector(-2, -4, -6)
    assert True == ( expected == (t1 - t2))
    
def test_tuples_negating_tuples():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(-1, 2, -3, 4)
    assert True == ( expected == -t1)
    
def test_tuples_multiplying_tuples_scalar():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(3.5, -7, 10.5, -14)
    assert True == ( expected == t1 * 3.5)
    
def test_tuples_multiplying_tuples_scalar_2():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(0.5, -1, 1.5, -2)
    assert True == ( expected == t1 * 0.5)
    
def test_tuples_dividing():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(0.5, -1, 1.5, -2)
    assert True == ( expected == t1 / 2)

def test_tuples_compute_magnitude():
    t1 = Tuples(1,0,0,0)
    assert True == ( t1.equal(t1.magnitude(t1),1))
 
def test_tuples_compute_magnitude2():
    t1 = Tuples(0,1,0,0)
    assert True == ( t1.equal(t1.magnitude(t1),1))   
    
def test_tuples_compute_magnitude3():
    t1 = Tuples(0,0,1,0)
    assert True == ( t1.equal(t1.magnitude(t1),1))  
    
def test_tuples_compute_magnitude4():
    t1 = Tuples(1,2,3,0)
    assert True == ( t1.equal(t1.magnitude(t1),sqrt(14)))   
    
def test_tuples_compute_magnitude5():
    t1 = Tuples(-1,-2,-3,0)
    assert True == ( t1.equal(t1.magnitude(t1),sqrt(14)))   
    
def test_tuples_normalizing_vector():
    t1 = Tuples()
    t1.Vector(4,0,0)
    expected = Tuples()
    expected.Vector(1,0,0)
    assert True == (expected == t1.normalize(t1))
    
def test_tuples_normalizing_vector2():
    t1 = Tuples()
    t1.Vector(1,2,3)
    expected = Tuples()
    expected.Vector(1/sqrt(14),2/sqrt(14),3/sqrt(14))
    assert True == (expected == t1.normalize(t1))  
    
def test_tuples_normalizing_vector3():
    t1 = Tuples()
    t1.Vector(1,2,3)
    normalized = t1.normalize(t1)
    assert True == (normalized.equal(1, normalized.magnitude(normalized)))  
    
def test_tuples_dot_product_vectors():
    t1 = Tuples()
    t2 = Tuples()
    t1.Vector(1,2,3)
    t2.Vector(2,3,4)
    assert True == (t1.dot(t1,t2) == 20)
    
def test_tuples_cross_product_vectors():
    t1 = Tuples()
    t2 = Tuples()
    t1.Vector(1,2,3)
    t2.Vector(2,3,4)
    expected1 = Tuples()
    expected1.Vector(-1,2,-1)
    expected2 = Tuples()
    expected2.Vector(1,-2,1)
    assert True == (t1.cross(t1,t2) == expected1)
    assert True == (t1.cross(t2,t1) == expected2)
    
def test_tuples_reflecting_vector_45():
    t1 = Tuples()
    t2 = Tuples()
    expected = Tuples()
    t1.Vector(1, -1, 0)
    t2.Vector(0, 1, 0)
    expected.Vector(1, 1, 0)
    assert True == (t1.reflect(t1, t2) == expected) 

def test_tuples_reflecting_vector_slanted_surface():
    t1 = Tuples()
    t2 = Tuples()
    expected = Tuples()
    t1.Vector(0, -1, 0)
    t2.Vector(sqrt(2)/2, sqrt(2)/2, 0)
    expected.Vector(1, 0, 0)
    assert True == (t1.reflect(t1, t2) == expected) 