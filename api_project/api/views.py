from django.shortcuts import render
# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Use the Book model's queryset
    serializer_class = BookSerializer  # Use the BookSerializer

# Create your views here.
