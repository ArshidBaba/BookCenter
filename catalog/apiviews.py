from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         data = BookSerializer(book).data
#         return Response(data)

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        data = BookSerializer(books, many=True).data
        return Response(data)

class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        data = AuthorSerializer(authors, many=True).data
        return Response(data)