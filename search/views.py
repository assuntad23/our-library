from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class BookResponse(serializers.Serializer):
    id = serializers.IntegerField(source='pk')
    title = serializers.CharField()
    author_first = serializers.CharField()
    author_last = serializers.CharField()
    fiction = serializers.BooleanField()
    condition = serializers.CharField()
    assunta_read = serializers.BooleanField()
    lucian_read = serializers.BooleanField()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author_first', 'author_last', 'fiction', 'condition', 'assunta_read', 'lucian_read']


# Step 2: Update the view
class AllView(APIView):
    def get(self, request):
        all_objects = Book.objects.all()
        serialized_data = BookResponse(all_objects, many=True).data
        return Response(serialized_data)
    

class AddBook(LoginRequiredMixin, APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SearchByTitle(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        if not title: 
            return Response ({"error": "No such title exists"})
        books = Book.objects.filter(title__icontains=title)
        if books.exists():
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"message": "No books found"}, status=status.HTTP_404_NOT_FOUND)