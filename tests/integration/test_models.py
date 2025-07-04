from bookstore.database import UserCredentials, Book

def test_user_credentials_model():
    user = UserCredentials(email="test@example.com", password="testpass")
    assert user.email == "test@example.com"
    assert user.password == "testpass"

def test_book_model():
    book = Book(name="My Book", author="Author Name", published_year=2024, book_summary="Summary")
    assert book.name == "My Book"
    assert book.author == "Author Name"
    assert book.published_year == 2024
    assert book.book_summary == "Summary"
