from src.task2 import get_integer, get_float, get_string, get_boolean

def test_integer():
    result = get_integer()
    assert type(result) == int
    assert result == 42

def test_float():
    result = get_float()
    assert type(result) == float
    assert result == 3.14

def test_string():
    result = get_string()
    assert type(result) == str
    assert result == "Hello, Python!"

def test_boolean():
    result = get_boolean()
    assert type(result) == bool
    assert result == True
