# relationship_app/urls.py
from django.urls import path
from .views import RegisterView, ListBooksView, AddBookView, EditBookView, DeleteBookView
from .admin_view import admin_view  # This should be correct

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', ListBooksView.as_view(), name='list_books'),
    path('books/add/', AddBookView.as_view(), name='add_book'),
    path('books/edit/<int:book_id>/', EditBookView.as_view(), name='edit_book'),
    path('books/delete/<int:book_id>/', DeleteBookView.as_view(), name='delete_book'),
    path('admin/', admin_view, name='admin_view'),
]