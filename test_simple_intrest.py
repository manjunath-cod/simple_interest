from simple_intrest import simple_interest
def test_simple_interest():
    assert simple_interest(1000, 1.9, 1) == 19.0
    assert simple_interest(2000, 10, 3) == 600.0
    assert simple_interest(3000, 7, 4) == 840.0
    
def test_zero_interest():
    assert simple_interest(1000, 0, 1) == 0.0
def test_zero_principal():
    assert simple_interest(0, 5, 1) == 0.0
def test_zero_time():
    assert simple_interest(1000, 5, 0) == 0.0

def test_large_values():
    assert simple_interest(1000000, 5, 10) == 500000.0