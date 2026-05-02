from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse


from api.models import Category
from api.serializers import CategorySerializer


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="ali", password="****")
        self.category1 = Category.objects.create(
            name="Badiiy adabiyot", description=" 11 ", is_staff=True
        )
        self.category2 = Category.objects.create(
            name="Jahon adabiyoti", description=" 22 ", is_staff=True
        )
        self.category3 = Category.objects.create(
            name="Jadidlar Merosi", description=" 33 ", is_staff=True
        )

    def test_not_is_authenticated(self):
        url = reverse("category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get(self):
        url = reverse("category-list")

        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer(
            [self.category1, self.category2, self.category3], many=True
        )

        self.assertEqual(response.json(), serializer.data)

    def test_one_get(self):
        url = reverse("category-detail", args=[self.category1.pk])

        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer(self.category1)

        self.assertEqual(response.json(), serializer.data)

        self.assertEqual(response.json(), serializer.data)


# from unittest import TestCase


# def add(a, b):
#     return a + b


# class AddTestCase(TestCase):
#     def test_add(self):
#         res = add(4, 9)
#         self.assertEqual(res, 13)
#         self.assertNotEqual(res, 10)
