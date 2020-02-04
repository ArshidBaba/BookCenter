from rest_framework import serializers

from .models import Book, Author, Genre, BookInstance

class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # book_inst = BookInstanceSerializer(many=True)
    # data = book_inst[0][]
    # name = serializers.CharField(source="first_name.title", read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    # authors = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')

class GenreSerializer(serializers.ModelSerializer):
    # genres = BookSerializer(many=True)
    class Meta:
        model = Genre
        fields = '__all__'

