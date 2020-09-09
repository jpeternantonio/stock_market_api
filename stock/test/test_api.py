import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse, include, path
from stock.models import Stocks, Purchased
from account.models import User
from stock.api.serializers import StockSerializer, PurchasedSerializer
from decimal import Decimal
from rest_framework.test import APITestCase, APIClient


class StockTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'john'
        self.password = 'Test1234.'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        Stocks.objects.create(name='microsoft', price=Decimal('144.15'))


    def test_get_stock_list(self):
        response = self.client.get('/api/stocks/', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_create_stock(self):
        data = {'name': 'Asus', 'price':46.45}
        response = self.client.post('/api/stock/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_get_stock_detail(self):
        response = self.client.get('/api/stocks/1/', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PurchasedTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'james'
        self.password = 'Test1234.'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        Stocks.objects.create(name='microsoft', price=Decimal('144.15'))


    def purchased_post(self):
        data = {'user_id': 1, 'stock_id': 1, 'price':46.45, 'share':3}
        response = self.client.post('/api/buy/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def purchased_get(self):
        response = self.client.get('/api/purchased/1/', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def sell(self):
        data = {'user_id': 1, 'stock_id': 1, 'price':46.45, 'share':2}
        response = self.client.put('/api/sell/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


