# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register BookViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include all routes registered with the router
]