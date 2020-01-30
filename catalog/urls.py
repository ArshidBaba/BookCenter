from django.contrib import admin
from django.urls import path, include

from .apiviews import BookList, AuthorList

urlpatterns = [
    path('', BookList.as_view(), name='index'),
    path('authors/', AuthorList.as_view(), name='authors')
    # path('catalog/<int:pk>/', views.index, name="catalog" )
]