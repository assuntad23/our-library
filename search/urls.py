from django.urls import path, include
from .views import AllView, SearchByTitle

urlpatterns = [
    path('all/', AllView.as_view(), name='all_books'),
    path('', SearchByTitle.as_view(), name='search_by_title')
]
