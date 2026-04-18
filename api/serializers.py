from rest_framework import serializers

from .models import Category, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
        read_only_fields = ("id",)

    def validate_name(self, value: str):
        if value.istitle():
            raise serializers.ValidationError("Nomi bosh harfda bo'lishi kerak")

        return value


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ("anotation",)

    def validate_name(self, value):
        if value.istitle():
            raise serializers.ValidationError(
                "Nomi bosh harfi katta harf bo'lishi kerak"
            )

        return value

    def validate_author(self, value):
        if not value.istitle():
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
