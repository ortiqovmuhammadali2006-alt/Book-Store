from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import BookViewSet, CategoryViewSet, CommentViewSet



router = DefaultRouter()

router.register('books', BookViewSet, basename='book')
router.register('category', CategoryViewSet, basename='category')
router.register('comment', CommentViewSet, basename='comment')




urlpatterns = router.urls


