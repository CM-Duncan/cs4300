"Caroline Duncan, 2/13/26,  checks: the number of books returned, that each book has the required title and author fields, and the structure of the student database. "
from src.task5 import get_favorite_books, get_first_three_books, get_student_database

def test_favorite_books_length():
    books = get_favorite_books()
    assert len(books) == 5

def test_favorite_books_has_title_and_author():
    books = get_favorite_books()
    for book in books:
        assert "title" in book
        assert "author" in book

def test_first_three_books():
    first_three = get_first_three_books()
    assert len(first_three) == 3

def test_student_database():
    students = get_student_database()
    assert type(students) == dict
    assert students["Alice"] == "S001"
    assert students["Bob"] == "S002"
    assert students["Charlie"] == "S003"
