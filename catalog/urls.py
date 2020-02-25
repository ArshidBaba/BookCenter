from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apiviews import GenreViewSet, AuthorViewSet, BookList, BookDetail, AuthorList, BookViewSet,\
 Query, UserCreate
# , queryapi \
# , QueryViewSet
# from rest_framework_swagger.views import get_swagger_view



router = DefaultRouter()
router.register('books', BookViewSet)
router.register('genres', GenreViewSet)
# router.register('<int:pk>/', BookInstanceViewSet)
router.register('authors', AuthorViewSet)
# router.register('query', QueryViewSet)

# schema_view = get_swagger_view(title='Book Center')

urlpatterns = [
    # path('books/', BookList.as_view(), name='books'),
    # path('authors/', AuthorList.as_view(), name='authors'),
    # path('catalog/<int:pk>/', BookInstanceViewSet.as_view(), name="catalog" )
    # path('swagger-docs/', schema_view),
    path('queries', Query.as_view(), name='queries'),
    path('users/', User)
]

urlpatterns += router.urls