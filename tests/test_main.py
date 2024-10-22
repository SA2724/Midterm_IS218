'''My Calculator Test'''
from app.main import addition
def test_addition():
    '''Addition Function'''
    assert addition(1,1) == 2
