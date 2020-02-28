from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from .apiviews import GenreViewSet, AuthorViewSet, BookList, BookDetail, AuthorList, BookViewSet,\
Query,  LoginView, UserView
# UserCreate 




# , queryapi \
# , QueryViewSet
# from rest_framework.schemas import get_schema_view



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
    # path('openapi', get_schema_view(
    #     title="BookCenter",
    #     description="API for all things …"
    # ), name='openapi-schema'),
    path('queries', Query.as_view(), name='queries'),
    # path('users/', UserCreate.as_view(), name='user_create'),
    path('users/', UserView.as_view(), name='user_view'),
    path('login/', LoginView.as_view(), name='login'),
    path(r'docs/', include_docs_urls(title="BookCenter"))
]

urlpatterns += router.urls