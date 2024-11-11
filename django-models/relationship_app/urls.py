from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, RegisterView  # Import your custom views
# relationship_app/urls.py
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
# relationship_app/urls.py
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('book/add/', add_book, name='add_book'),  # URL for adding a book
    path('book/edit/<int:book_id>/', edit_book, name='edit_book'),  # URL for editing a book
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),  # URL for deleting a book
]

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('admin/', admin_view, name='admin_view'),  # URL for Admin view
    path('librarian/', librarian_view, name='librarian_view'),  # URL for Librarian view
    path('member/', member_view, name='member_view'),  # URL for Member view
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library details
    path('register/', RegisterView.as_view(), name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # URL for user login
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html', next_page='login'), name='logout'),  # URL for user logout
]

