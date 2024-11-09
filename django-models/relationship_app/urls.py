from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, RegisterView 
# relationship_app/urls.py

from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),  # URL for Admin view
    path('librarian/', librarian_view, name='librarian_view'),  # URL for Librarian view
    path('member/', member_view, name='member_view'),  # URL for Member view
] # Import your custom views

urlpatterns = [
    ["views.register"]
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library details
    path('register/', RegisterView.as_view(), name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # URL for user login
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html', next_page='login'), name='logout'),  # URL for user logout
]

