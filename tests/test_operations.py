from src.math_operators import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(3,7)==10
    
def test_sub():
    assert sub(2,3)==-1
    assert sub(-1,1)==-2
    assert sub(3,3)==0