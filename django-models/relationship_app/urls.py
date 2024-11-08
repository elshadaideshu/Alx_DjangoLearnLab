from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, RegisterView  # Ensure RegisterView is imported

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for the function-based view to list books
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based library detail view
    path('register/', RegisterView.as_view(), name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # URL for user login
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html', next_page='login'), name='logout'),  # URL for user logout
]