import json

from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse


from api.models import Category
from api.serializers import CategorySerializer


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ali", password="123456")
        self.login_url = reverse("login")
        response = self.client.post(
            self.login_url, data={"username": "ali", "password": "123456"}
        )

        token = response.json()["auth_token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)
        

        self.category1 = Category.objects.create(
            name="Badiiy adabiyot", description=" 11 ", is_staff=True
        )
        self.category2 = Category.objects.create(
            name="Jahon adabiyoti", description=" 22 ", is_staff=True
        )
        self.category3 = Category.objects.create(
            name="Jadidlar + Jahon adabiyotlari Merosi",
            description=" 33 ",
            is_staff=True,
        )

    # def test_not_is_authenticated(self):
    #     url = reverse("category-list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get(self):
        url = reverse("category-list")

        # self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer(
            [self.category1, self.category2, self.category3], many=True
        )

        self.assertEqual(response.json(), serializer.data)

    def test_one_get(self):
        url = reverse("category-detail", args=[self.category1.pk])

        # self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer(self.category1)

        self.assertEqual(response.json(), serializer.data)

    def test_get_filter(self):
        url = reverse("category-list")

        # self.client.force_login(self.user)
        response = self.client.get(url, data={"is_staff": True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer(
            [self.category1, self.category2, self.category3], many=True
        )
        self.assertEqual(response.json(), serializer.data)

    def test_get_search(self):
        url = reverse("category-list")

        # self.client.force_login(self.user)
        response = self.client.get(url, data={"search": "Jahon"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer([self.category2, self.category3], many=True)
        self.assertEqual(response.json(), serializer.data)

    def test_get_ordering(self):
        url = reverse("category-list")

        # self.client.force_login(self.user)
        response = self.client.get(url, data={"ordering": "name"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = CategorySerializer(
            [self.category1, self.category3, self.category2], many=True
        )
        self.assertEqual(response.json(), serializer.data)

    def test_create(self):

        data = {"name": "Psixologiya", "description": "null", "is_staff": False}

        url = reverse("category-list")

        # self.client.force_login(self.user)
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Category.objects.all().count(), 4)

    def test_update(self):

        data = {
            "name": "Badiiy adabiyot Updated",
            "description": " 11 ",
            "is_staff": False,
        }

        url = reverse("category-detail", args=(self.category1.pk,))

        # self.client.force_login(self.user)
        response = self.client.put(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category1.refresh_from_db()
        self.assertEqual(self.category1.is_staff, False)
        # self.assertEqual(self.category1.name, "Badiiy adabiyot Updated")

        data = {
            "name": "Badiiy adabiyot Updated",
            "description": " 11 ",
            "is_staff": False,
        }

        url = reverse("category-detail", args=(self.category1.pk,))

        # self.client.force_login(self.user)
        response = self.client.put(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category1.refresh_from_db()
        self.assertEqual(self.category1.is_staff, False)

    def test_patch(self):

        data = {"is_staff": True}

        url = reverse("category-detail", args=(self.category1.pk,))

        # self.client.force_login(self.user)
        response = self.client.patch(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category1.refresh_from_db()
        self.assertEqual(self.category1.is_staff, True)

    def test_delete(self):

        url = reverse("category-detail", args=(self.category1.pk,))

        # self.client.force_login(self.user)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
