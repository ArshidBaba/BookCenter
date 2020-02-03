from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apiviews import  BookViewSet, GenreViewSet, BookInstanceViewSet, AuthorViewSet
# from rest_framework_swagger.views import get_swagger_view



router = DefaultRouter()
router.register('books', BookViewSet)
router.register('genres', GenreViewSet)
router.register('<int:pk>/', BookInstanceViewSet)
router.register('authors', AuthorViewSet)


# schema_view = get_swagger_view(title='Book Center')

urlpatterns = [
    # path('', BookList.as_view(), name='index'),
    # path('authors/', AuthorList.as_view(), name='authors'),
    # path('catalog/<int:pk>/', BookInstanceViewSet.as_view(), name="catalog" )
    # path('swagger-docs/', schema_view),
]

urlpatterns += router.urls