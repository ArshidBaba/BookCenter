from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apiviews import BookList, AuthorList, BookViewSet

router = DefaultRouter()
router.register('catalog', BookViewSet)

urlpatterns = [
    # path('', BookList.as_view(), name='index'),
    path('authors/', AuthorList.as_view(), name='authors')
    # path('catalog/<int:pk>/', views.index, name="catalog" )
]

urlpatterns += router.urls