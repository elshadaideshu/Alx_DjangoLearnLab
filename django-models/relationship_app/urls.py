# relationship_app/urls.py
from django.urls import path
from .views import RegisterView, ListBooksView, AddBookView, EditBookView, DeleteBookView
from .admin_view import admin_view
from django.contrib import admin
from django.urls import path, include
from .views import list_books, LibraryDetailView, register, user_login, user_logout
from .views import admin_view, librarian_view, member_view



urlpatterns = [
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