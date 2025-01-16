from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author_first', 'author_last', 'fiction', 'condition', 'assunta_read', 'lucian_read']

class AddBook(LoginRequiredMixin, APIView):
    def post(self, request):
        title = request.data.get('title')
        author_first = request.data.get('author_first')
        author_last = request.data.get('author_last')
        if Book.objects.filter(Q(title=title) & Q(author_first=author_first) & Q(author_last=author_last)).exists():
            return Response(
                {"error": "A book with this title and author already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteBook(LoginRequiredMixin, APIView):
    def delete(self, request, pk):
        # Find the book using its primary key (id)
        book = get_object_or_404(Book, pk=pk)
        
        book.delete()
        return Response({"message": "Book '{book.title}' deleted successfully."}, status=status.HTTP_204_NO_CONTENT)