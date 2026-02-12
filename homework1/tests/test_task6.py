from src.task6 import count_words

def test_count_words():
    result = count_words("task6_read_me.txt")
    assert result == 100

