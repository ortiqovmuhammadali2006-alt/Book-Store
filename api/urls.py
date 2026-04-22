from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import BookViewSet, CategoryViewSet

# router = SimpleRouter()

router = DefaultRouter()

router.register('books', BookViewSet, basename='book')
router.register('category', CategoryViewSet, basename='category')

#3-usul

urlpatterns = router.urls



#2-usul
# urlpatterns = [
#     path('', include(router.urls))
# ]

#o'zimizani usul
# urlpatterns = [
#     path(
#         "books/", BookViewSet.as_view({"get": "list", "post": "create"}), name="books"
#     ),
#     path(
#         "books/<int:pk>/",
#         BookViewSet.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#         name="book_detail",
#     ),
#     path(
#         "category/",
#         CategoryViewSet.as_view({"get": "list", "post": "create"}),
#         name="category",
#     ),
#     path(
#         "category/<int:pk>/",
#         CategoryViewSet.as_view(
#             {
#                 "get": "retrieve",
#                 "put": "update",
#                 "patch": "partial_update",
#                 "delete": "destroy",
#             }
#         ),
#         name="category_detail",
#     ),
# ]
