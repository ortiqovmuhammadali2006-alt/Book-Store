from rest_framework.viewsets import ModelViewSet


from .models import Category, Book, Comment
from .serializers import (
    CategorySerializer,
    BookSerializer,
    CommentSerializer,
    CategorySerializerForDetail,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().prefetch_related("books")
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return CategorySerializerForDetail
        else:
            return CategorySerializer


class BookViewSet(ModelViewSet):
    queryset = (
        Book.objects.all()
        .prefetch_related("category")
        .select_related("comment")
        .only()  # kerakli ma'lumotlarni databasedan olish uchun only() ishlatiladi
    )

    # queryset = (
    #     Book.objects.all()
    #     .prefetch_related("category")
    #     .select_related("comment")
    #     .defer()  # keraksiz ma'lumotlarni databasedan olish uchun defer() ishlatiladi
    # )
    serializer_class = BookSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
