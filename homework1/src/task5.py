"Caroline Duncan, 2/13/26, returns a hardcoded list of five classic books, each represented as a dictionary "
def get_favorite_books():
    books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger"}
    ]
    return books

def get_first_three_books():
    books = get_favorite_books()
    return books[:3]

def get_student_database():
    students = {
        "Alice": "S001",
        "Bob": "S002",
        "Charlie": "S003"
    }
    return students
