from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase
from books.models import Book
from rest_framework import status

class AuthenticationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        
        self.book = Book.objects.create(
            title="Test Book",
            author_first="John",
            author_last="Doe",
            fiction=True,
            condition="VG",
            assunta_read=True,
            lucian_read=False,
        )

    def test_add_book_authenticated(self):
        self.client.login(username='testuser', password='password')
    
        data = {
            'title': 'New Test Book',
            'author_first': 'Jane',
            'author_last': 'Smith',
            'fiction': True,
            'condition': 'N',
            'assunta_read': False,
            'lucian_read': False
        }
    
        response = self.client.post('/books/add/', data, format='json')
    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_book_requires_authentication(self):
        data = {
            'title': 'New Test Book',
            'author_first': 'Jane',
            'author_last': 'Smith',
            'fiction': True,
            'condition': 'N',
            'assunta_read': False,
            'lucian_read': False
        }

        response = self.client.post('/books/add/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_book_requires_authentication(self):
        response = self.client.delete(f'/books/{self.book.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password')

        response = self.client.delete(f'/books/{self.book.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
