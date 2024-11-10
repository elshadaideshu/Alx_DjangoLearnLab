from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),  # Correct import
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]