# relationship_app/urls.py
from django.urls import path
from .views import RegisterView, ListBooksView, AddBookView, EditBookView, DeleteBookView
from .admin_view import admin_view  # Assuming you have this view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', ListBooksView.as_view(), name='list_books'),
    path('books/add/', AddBookView.as_view(), name='add_book'),  # URL for adding a book
    path('books/edit/<int:book_id>/', EditBookView.as_view(), name='edit_book'),  # URL for editing a book
    path('books/delete/<int:book_id>/', DeleteBookView.as_view(), name='delete_book'),  # URL for deleting a book
    path('admin/', admin_view, name='admin_view'),  # Admin view
]