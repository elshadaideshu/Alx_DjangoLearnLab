# Delete Operation

## Command
```python
book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book instance
book.delete()                                           # Delete the book

books = Book.objects.all()
print(books)  # Check if the book is deleted