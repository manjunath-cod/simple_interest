from simple_intrest import simpleint

def test_1():
    assert simpleint(1000,30,4) == 1200

def test_2():
    assert simpleint(2000,5,6) == 600

def test_3():
    assert simpleint(10000,30,10) == 30000