# api/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Use the Book model's queryset
    serializer_class = BookSerializer  # Use the BookSerializer