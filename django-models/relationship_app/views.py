from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'list_books.html', {'books': books})
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Library

# Class-based view to display library details
class LibraryDetailView(View):
    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)  # Get the library by primary key
        return render(request, 'library_detail.html', {'library': library})