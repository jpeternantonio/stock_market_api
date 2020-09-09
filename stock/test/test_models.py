from django.test import TestCase
from stock.models import Stocks, Purchased
from account.models import User
from decimal import Decimal
from django.db.models import F


class StockTestCase(TestCase):
   
    def setUp(self) -> None:
        Stocks.objects.create(name="pldt", price=Decimal('9.53'))
        Stocks.objects.create(name='kfc', price=Decimal('11.52'))

    def test_stock_price(self) -> bool:
        pldt = Stocks.objects.get(name="pldt")
        kfc = Stocks.objects.get(name='kfc')
        self.assertEqual(pldt.price, Decimal('9.53'))
        self.assertEqual(kfc.price, Decimal('11.52'))


class PurchasedTestCase(TestCase):

    def setUp(self) -> None:
        user = User.objects.create(username='john', password='Test456.', email='john@gmail.com', balance=5000)
        user.save()
        stock = Stocks.objects.create(name="allied", price=Decimal('12.67'))
        stock.save()
        user = User.objects.get(username='john')
        stock = Stocks.objects.get(name='allied')
        purchased = Purchased.objects.create(user_id=user.id, stock_id=stock.id, price=stock.price, share=2)
        purchased.save()
        

    # test for purchase transaction
    def test_purchased(self) -> bool:
        purchased = Purchased.objects.get(id=1)
        self.assertEqual(purchased.user.username, 'john')
        self.assertEqual(purchased.stock.name, 'allied')
        self.assertEqual(purchased.share, 2)
        self.assertEqual(purchased.price, Decimal('12.67'))
        self.assertEqual(purchased.user.balance, 5000)


class SellTestCase(TestCase):

    def setUp(self) -> None:
        user = User.objects.create(username='peter', password='Test456.', email='john@gmail.com', balance=5000)
        user.save()
        stock = Stocks.objects.create(name="tesla", price=Decimal('50'))
        stock.save()
        user = User.objects.get(username='peter')
        stock = Stocks.objects.get(name='tesla')
        purchased = Purchased.objects.create(user_id=user.id, stock_id=stock.id, price=stock.price, share=2)
        purchased.save()
        

    # Testing of selling transaction, assertion were seperated to validate the field value specifically
    def test_sell(self) -> bool:
        sell = Purchased.objects.get(id=1)
        self.assertEqual(sell.price, Decimal('50'))

        update_stock = Stocks.objects.update(price=F('price') + 50) # Change of stock market price
        self.assertEqual(sell.stock.price, Decimal('100'))

        self.assertEqual(sell.user.balance, 5000)
        self.assertEqual(sell.share, 2)
        total = int(sell.share) * Decimal(str(sell.stock.price))
        sell.user.balance += total
        sell.share -= 2

        self.assertEqual(sell.share, 0)
        self.assertEqual(sell.user.balance, 5200)
        self.assertEqual(sell.user.username, 'peter')
        self.assertEqual(sell.stock.name, 'tesla')
        
        
        
    