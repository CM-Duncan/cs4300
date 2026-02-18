"Caroline Duncan, 2/11/12"
from src.task1 import hello_world

def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
