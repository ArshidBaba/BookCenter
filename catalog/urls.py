from django.contrib import admin
from django.urls import path, include

from .apiviews import BookList

urlpatterns = [
    path('', BookList.as_view(), name='index'),
    # path('catalog/<int:pk>/', views.index, name="catalog" )
]