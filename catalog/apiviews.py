from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import JsonResponse
from django.core import serializers


from .models import Book, Author, Genre, BookInstance, Query
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, BookInstanceSerializer, QuerySerializer
from .tasks import send_email_task

class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)

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

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# class GenreList(APIView):
#     def get(self, request):
#         genres = Genre.objects.all()
#         data = GenreSerializer(genres, many=True).data
#         return Response(data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer   

# class QueryDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'query_form.html'

#     def get(self, request):
#         serializer_class = QuerySerializer()

#     def post(self, request):
#         serializer_class = QuerySerializer(data=request.data)
#         serializer_class.save()
#         return redirect('books')

# class QueryViewSet(viewsets.ModelViewSet):
#     queryset = Query.objects.all()
#     serializer_class = QuerySerializer

@api_view(['POST'])
def queryapi(request):
    if request.method == 'POST':
        # data = request.data
        print(request.data)
        # response_data['text'] = serializers.serialize('json', request)
        # send_email_task.delay(JsonResponse(response_data, safe=False))
        # return Response({"message": "Got some data!", "data": request.data})
        return Response({"Query has been sent": request.data})
    return Response({"Welcome to Query page"})