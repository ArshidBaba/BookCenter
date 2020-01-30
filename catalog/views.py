from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Book



def index(request):
    books = Book.objects.all()
    # books = get_object_or_404(Book, pk=pk)
    data = { 'books': list(
        books.values('title', 'author')
    )
    }
    return JsonResponse(data, safe=False)
