from django.urls import path

from .views import (
    BookCreate,
    BookListView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    BookRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("books/", BookListView.as_view(), name="books"),
    path("books/create/", BookCreate.as_view(), name="book_create"),
    path('book/detail/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book_detail'),


    path("category/", CategoryListCreateView.as_view(), name="categories"),
    path(
        "category/detail/<int:pk>/",
        CategoryRetrieveUpdateDestroyView.as_view(),
        name="category_detail",
    ),
]
