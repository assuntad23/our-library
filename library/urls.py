"""
URL configuration for library project.

landing_page is main page where users can search for books, and add/delete if logged in
/search is where users can search for books based on title or return all TODO: search by author
/admin is boilerplate Django login and admin of DB
/books is the endpoint for adding or deleting a book  TODO: update existing book
"""

from django.contrib import admin
from django.urls import include, path
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path("search/", include("search.urls")),
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")),
    path('accounts/', include('allauth.urls'))
]
