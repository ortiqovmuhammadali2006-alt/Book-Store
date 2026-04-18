from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    anotation = models.TextField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


        


