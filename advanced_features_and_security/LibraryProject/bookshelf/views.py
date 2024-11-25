# LibraryProject/bookshelf/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm  # Assume you have a form for Book
# LibraryProject/bookshelf/views.py
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Here you can add logic to save the data or perform other actions
            return redirect('success_page')  # Redirect to a success page or another view
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/example_form.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)  # Securely parameterized query
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
# views.py
# Permissions are enforced using the @permission_required decorator.
# Users must have specific permissions based on their assigned groups:
# - Editors: can_create, can_edit
# - Viewers: can_view
# - Admins: can_view, can_create, can_edit, can_delete