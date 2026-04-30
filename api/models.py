from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=250)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user"
    )
    rating = models.PositiveBigIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    text = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    anotation = models.TextField(max_length=200)
    is_active = models.BooleanField(default=False)    
    category = models.ManyToManyField(Category, related_name="books")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name



