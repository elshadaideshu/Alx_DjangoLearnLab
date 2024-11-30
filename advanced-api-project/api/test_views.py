# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User
# api/test_views.py

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a Book instance for testing
        self.book = Book.objects.create(title='Test Book', author='Author Name', publication_year=2023)

    def tearDown(self):
        self.book.delete()
def test_create_book(self):
    url = reverse('book-create')
    data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2024}
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 2)  # Check if the book count increased
def test_list_books(self):
    url = reverse('book-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)  # Should return 1 book
def test_retrieve_book(self):
    url = reverse('book-detail', args=[self.book.id])
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], self.book.title)  # Check title
def test_delete_book(self):
    url = reverse('book-delete', args=[self.book.id])
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 0)  # Check if the book was deleted
def test_unauthorized_create_book(self):
    self.client.logout()  # Log out the user
    url = reverse('book-create')
    data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2024}
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)