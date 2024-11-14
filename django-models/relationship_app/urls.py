# relationship_app/urls.py
from django.urls import path
from .views import RegisterView, ListBooksView, AddBookView, EditBookView, DeleteBookView
from .admin_view import admin_view
from django.contrib import admin
from django.urls import path, include
from .views import list_books, LibraryDetailView, register, user_login, user_logout
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book, list_books  # Assuming you have a list_books view # Import your views



urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('books/', list_books, name='list_books'),
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', ListBooksView.as_view(), name='list_books'),
    path('books/add/', AddBookView.as_view(), name='add_book'),  # URL for adding a book
    path('books/edit/<int:book_id>/', EditBookView.as_view(), name='edit_book'),  # URL for editing a book
    path('books/delete/<int:book_id>/', DeleteBookView.as_view(), name='delete_book'),  # URL for deleting a book
    path('admin/', admin_view, name='admin_view'),  # Admin view
]