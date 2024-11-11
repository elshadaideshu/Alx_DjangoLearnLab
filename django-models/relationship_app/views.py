# relationship_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .forms import UserRegistrationForm, BookForm
from .models import Book
# relationship_app/admin_view.py
from django.shortcuts import render

def admin_view(request):
    return render(request, 'relationship_app/admin.html')  # Ensure this template exists

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('list_books')
        return render(request, 'relationship_app/register.html', {'form': form})

class ListBooksView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'relationship_app/list_books.html', {'books': books})

@method_decorator(permission_required('relationship_app.can_add_book'), name='dispatch')
class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'relationship_app/add_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
        return render(request, 'relationship_app/add_book.html', {'form': form})

@method_decorator(permission_required('relationship_app.can_change_book'), name='dispatch')
class EditBookView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(instance=book)
        return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
        return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@method_decorator(permission_required('relationship_app.can_delete_book'), name='dispatch')
class DeleteBookView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'relationship_app/delete_book.html', {'book': book})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('list_books')