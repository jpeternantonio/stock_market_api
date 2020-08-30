from django.test import TestCase
from stock.models import Stocks, Purchased
from account.models import User
from decimal import Decimal

class StockTestCase(TestCase):
   

    def setUp(self):
        Stocks.objects.create(name="pldt", price=Decimal('9.53'))
        Stocks.objects.create(name='kfc', price=Decimal('11.52'))

    def test_stock_price(self):
        pldt = Stocks.objects.get(name="pldt")
        kfc = Stocks.objects.get(name='kfc')
        self.assertEqual(pldt.price, Decimal('9.53'))
        self.assertEqual(kfc.price, Decimal('11.52'))


class PurchasedTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='john', password='Test456.', email='john@gmail.com', balance=5000)
        user.save()
        stock = Stocks.objects.create(name="allied", price=Decimal('12.67'))
        stock.save()
        user = User.objects.get(username='john')
        stock = Stocks.objects.get(name='allied')
        purchased = Purchased.objects.create(user_id=user.id, stock_id=stock.id, price=stock.price, share=2)
        purchased.save()
        

    def test_purchased(self):
        purchased = Purchased.objects.get(id=1)
        self.assertEqual(purchased.user.username, 'john')
        self.assertEqual(purchased.stock.name, 'allied')
        self.assertEqual(purchased.share, 2)
