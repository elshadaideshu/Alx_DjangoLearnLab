# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
# api/urls.py
from .views import BookViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('auth/token/', CustomObtainAuthToken.as_view(), name='api-token-auth'),  # Token retrieval endpoint
    path('', include(router.urls)),  # Include all routes registered with the router
]
