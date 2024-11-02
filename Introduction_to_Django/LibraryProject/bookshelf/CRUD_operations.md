# Create a Book instance
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
### 2. Retrieve Operation

**Command**:
```python
# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
    ### 3. Update Operation

**Command**:
```python
# Update the title of the book
book = Book.objects.get(title="1984")  # Retrieve the book instance
book.title = "Nineteen Eighty-Four"      # Update the title
book.save()                              # Save the changes
### 4. Delete Operation

**Command**:
```python
# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book instance
book.delete()                                           # Delete the book

# Confirm deletion
books = Book.objects.all()
print(books)  # This should return an empty queryset if the book is deleteds