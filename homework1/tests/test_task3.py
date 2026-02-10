from src.task3 import check_number, first_ten_primes, sum_one_to_hundred

def test_positive():
    assert check_number(5) == "positive"

def test_negative():
    assert check_number(-3) == "negative"

def test_zero():
    assert check_number(0) == "zero"

def test_first_ten_primes():
    assert first_ten_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_one_to_hundred():
    assert sum_one_to_hundred() == 5050
