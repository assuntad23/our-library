from django.contrib import admin

from books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_first', 'author_last', 'fiction', 'condition')
    search_fields = ('title', 'author_first', 'author_last')
    list_filter = ('fiction', 'condition')

admin.site.register(Book)