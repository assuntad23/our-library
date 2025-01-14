from django.urls import path, include
from .views import AddBook, DeleteBook

urlpatterns = [
    path('add/', AddBook.as_view()),
    path('<int:pk>', DeleteBook.as_view())
]