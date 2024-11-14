import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query to retrieve all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return None

# Query to list all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None

# Query to retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None

# Example usage
if __name__ == "__main__":
    # Replace with actual data for testing
    author_name = "Your Author Name"
    library_name = "Your Library Name"

    print("Books by Author:")
    books_by_author = get_books_by_author(author_name)
    if books_by_author:
        for book in books_by_author:
            print(book.title)
    else:
        print("Author not found.")

    print("\nBooks in Library:")
    books_in_library = get_books_in_library(library_name)
    if books_in_library:
        for book in books_in_library:
            print(book.title)
    else:
        print("Library not found.")

    print("\nLibrarian for Library:")
    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(librarian.name)
    else:
        print("Library not found.")