# Update Operation

## Command
```python
book = Book.objects.get(title="1984")  # Retrieve the book instance
book.title = "Nineteen Eighty-Four"      # Update the title
book.save()                              # Save the changes