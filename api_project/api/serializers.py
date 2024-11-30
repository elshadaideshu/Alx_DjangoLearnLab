# api/serializers.py

from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields

    def validate_publication_year(self, value):
        if value > 2023:  # Ensure the publication year is not in the future
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include name and related books
        # api/serializers.py
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields

    def validate_publication_year(self, value):
        if value > 2023:  # Ensure the publication year is not in the future
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value  # Return the validated value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nesting BookSerializer

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include name and related books