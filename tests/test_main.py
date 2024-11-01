'''My Calculator Test'''
from app.main import addition, multiplication, subtraction
def test_addition():
    '''Addition Function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''Subtraction Function'''
    assert subtraction(1,1) == 0

def test_multiplication():
    '''Multiplication Function'''
    assert multiplication (1,1) == 1
    