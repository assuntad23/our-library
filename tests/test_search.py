from django.test import TestCase
from books.models import Book  
from rest_framework.test import APIClient

class SearchTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title="Test Book",
            author_first="John",
            author_last="Doe",
            fiction=True,
            condition="VG",
            assunta_read=True,
            lucian_read=False
        )

    def test_search_returns_correct_book(self):
        response = self.client.get('/search/', {'title': 'Test'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), 1)  
        self.assertEqual(data[0]['title'], self.book.title)
        self.assertEqual(data[0]['author_first'], self.book.author_first)
        self.assertEqual(data[0]['author_last'], self.book.author_last)