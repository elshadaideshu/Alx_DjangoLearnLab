## Retrieve Operation

Command:
```python
retrieved_book = Book.objects.all()
for b in retrieved_book:
    print(b.title, b.author, b.publication_year)