import json
import unittest     
from django.test import TestCase, Client
from django.urls import reverse
from stock.models import Stocks, Purchased
from account.models import User


class TestViews(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        self.list_url = reverse('stock-list')
        self.purchased_url = reverse('buy_history')
        self.purchased_done_url = reverse('buy_done')
        self.sell_done_url = reverse('sell_done')
        self.user = User.objects.create_user('john', 'johndoe@gmail.com', 'Test456.')
        self.client.login(username='john', password='Test456.')


    def test_stock_list_GET(self) -> bool:
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/index.html')

    def test_purchased_GET(self) -> bool:
        response = self.client.get(self.purchased_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/buy_history.html')

    def test_purchased_done_GET(self) -> bool:
        response = self.client.get(self.purchased_done_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/buy.html')

    def test_sell_done_GET(self) -> bool:
        response = self.client.get(self.sell_done_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/sell.html')
