

import pytest
from book import Book
from  library import  Library

library = Library()
new_book = Book("Finding Nemo","jhj")
user_name = "Nechami"
##search_term = "f"

def test_add_book():
    library.add_book(new_book)
    assert new_book in library.books;
@pytest.mark.book
def test_add_user():
    library.add_user(user_name)
    assert user_name in library.users;
@pytest.mark.skipif(user_name in library.users ,reason="there is no user")
def test_check_out_book():
    library.check_out_book(user_name,new_book)
    assert new_book.is_checked_out == True;
@pytest.mark.skip(reason="--------")
def test_return_book():
    library.return_book(user_name,new_book)
    assert  new_book.is_checked_out == False

@pytest.mark.parametrize("search_term, expected_titles", [
    ("f", ["Finding Nemo"]),
    ("a", ["A Tale of Two Cities"]),
])
def test_search_books(search_term,expected_titles):
    result = library.search_books(search_term)
    result_title = [book.title for book in result]
    assert result_title == expected_titles
