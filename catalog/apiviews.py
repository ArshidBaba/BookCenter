from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


from .models import Book, Author, Genre, BookInstance
# , Query
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, BookInstanceSerializer, UserSerializer
# , QuerySerializer
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer   

class Query(APIView):
    def get(self, request):
        # query = Book.objects.all()
        # data = BookSerializer(many=True).data
        return render(request, 'query_form.html')
    def post(self, request):
        email = request.POST.get('email')
        d = {"message": "<h1>You are a subcriber now</h1>"}
        print(email)
        print(type(email))
        send_email_task.delay(email)
        # return Response(request.POST['email'])
        return render(request, 'query_form.html')
        # return Response({"Query has been sent": text})

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)




