from django.test import SimpleTestCase
from django.urls import reverse, resolve
from stock.views import StockListView, buy_done, buy_history, buy_stock, sell, sell_done


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('stock-list')
        self.assertEquals(resolve(url).func.view_class, StockListView)


    def test_list_url_is_resolved(self):
        url = reverse('buy_done')
        self.assertEquals(resolve(url).func, buy_done)

    def test_list_url_is_resolved(self):
        url = reverse('buy_history')
        self.assertEquals(resolve(url).func, buy_history)
    
    def test_list_url_is_resolved(self):
        url = reverse('buy_stock')
        self.assertEquals(resolve(url).func, buy_stock)
    
    def test_list_url_is_resolved(self):
        url = reverse('sell')
        self.assertEquals(resolve(url).func, sell)
    
    def test_list_url_is_resolved(self):
        url = reverse('sell_done')
        self.assertEquals(resolve(url).func, sell_done)