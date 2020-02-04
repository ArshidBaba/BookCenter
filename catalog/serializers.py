from rest_framework import serializers

from .models import Book, Author, Genre, BookInstance

class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author',)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    # genres = BookSerializer(many=True)
    class Meta:
        model = Genre
        fields = '__all__'

