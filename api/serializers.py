from rest_framework import serializers

from .models import Category, Book, Comment


class CategoryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("name", "author", "price", "anotation", "is_active")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "description", "books")
        read_only_fields = ("id",)


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    comment = serializers.CharField(
        source="comment.rating", default=None, read_only=True
    )

    class Meta:
        model = Book
        fields = "__all__"

    def validate_name(self, value):
        if value.istitle():
            raise serializers.ValidationError(
                "Nomi bosh harfi katta harf bo'lishi kerak"
            )

        return value

    def validate_author(self, value):
        if value.istitle():
            raise serializers.ValidationError(
                "Muallifni ism-familiyasi bosh harfi katta harf bo'lishi kerak"
            )

        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Mahsulot narxi manfiy bo'lishi mumkin emas"
            )
        return value


class BookSerializerForCategoryDetail(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("name", "author", "price", "anotation", "is_active")


class CategorySerializerForDetail(serializers.ModelSerializer):
    books = BookSerializerForCategoryDetail(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "description", "books")
        read_only_fields = ("id",)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate_text(self, valeu: str):
        if not valeu.istitle:
            raise serializers.ValidationError(
                "Kiritlgan matnning bosh harfi katta harf bo'lish kerak"
            )
        return valeu

    def validate_rating(self, value: int):
        if value > 5 and value < 0:
            raise serializers.ValidationError(
                "0 dan kichik yoki 5 dan katta qiymat kirita olmaysiz"
            )
        return value
