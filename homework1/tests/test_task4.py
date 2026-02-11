from src.task4 import calculate_discount

def test_discount_with_integers():
    result = calculate_discount(100, 20)
    assert result == 80

def test_discount_with_floats():
    result = calculate_discount(99.99, 10.5)
    assert result == 89.49105

def test_discount_with_mixed_types():
    result = calculate_discount(100, 25.5)
    assert result == 74.5

def test_zero_discount():
    result = calculate_discount(50, 0)
    assert result == 50

def test_full_discount():
    result = calculate_discount(100, 100)
    assert result == 0
