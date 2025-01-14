from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from books.models import Book


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
        fields = ['id', 'title', 'author_first', 'author_last', 'fiction', 'condition', 'assunta_read', 'lucian_read']


# Step 2: Update the view
class AllView(APIView):
    def get(self, request):
        all_objects = Book.objects.all()
        serialized_data = BookResponse(all_objects, many=True).data
        return Response(serialized_data)
    
    
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