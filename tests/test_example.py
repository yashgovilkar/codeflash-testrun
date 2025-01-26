import pytest
from example import is_prime, slow_function, redundant_loop

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(97) == True
    
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(100) == False
    
    assert is_prime(0) == False
    assert is_prime(-1) == False

def test_slow_function():
    result = slow_function()
    assert isinstance(result, list)

    assert 2 in result
    assert 3 in result
    assert 5 in result
    assert 997 in result  
    
    assert 4 not in result
    assert 100 not in result
    assert len(result) == 168

def test_redundant_loop():
    result = redundant_loop()
    expected = sum(x**2 for x in range(10000)) / 10000
    assert result == expected
    assert isinstance(result, float) 