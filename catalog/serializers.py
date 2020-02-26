from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import Book, Author, Genre, BookInstance
# , Query

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

# class QuerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Query
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

















