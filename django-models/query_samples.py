import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')  # Replace with your project's settings module
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # Correctly accessing the librarian for the library
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

# Sample usage
if __name__ == "__main__":
    author_books = get_books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:", [book.title for book in author_books] if author_books else "No books found.")

    library_books = list_books_in_library("Main Library")
    print("Books in Main Library:", [book.title for book in library_books] if library_books else "No books found.")

    librarian = get_librarian_for_library("Main Library")
    print("Librarian for Main Library:", librarian.name if librarian else "No librarian found.")