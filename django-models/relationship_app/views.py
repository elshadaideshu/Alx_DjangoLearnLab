from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library 
from .models import Library
from django.views.generic.detail import DetailView # Import both Book and Library models

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the template with the books context

# Class-based view to display library details
class LibraryDetailView(View):
    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)  # Get the library by primary key
        return render(request, 'relationship_app/library_detail.html', {'library': library})  # Render the library detail template

# User Registration View
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('list_books')  # Redirect to the list of books after registration
        return render(request, 'registration/register.html', {'form': form})