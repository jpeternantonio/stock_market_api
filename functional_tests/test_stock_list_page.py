import time
from selenium import webdriver
from stock.models import Stocks
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from pyvirtualdisplay import Display
from decimal import Decimal

display = Display(visible=0, size=(800, 800))  
display.start()
driver = webdriver.Chrome()




class TestStockListPage(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.browser = driver

    def tearDown(self) -> None:
        self.browser.close()

    def test_no_stock_list_page(self) -> bool:
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_class_name('check_stock')
        
        # the user requests the page for the first time
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            'No stocks yet. Ask admin.'
        )

    def test_no_stock_list_add_page(self) -> bool:
        self.browser.get(self.live_server_url)

        # the user requests the page for the first time and navigate the add button
        add_url = self.live_server_url + reverse('/admin/')
        self.browser.find_element_by_class_name('add_stock').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_user_sees_stock_list(self) -> bool:
        stock_1 = Stocks.objects.create(
            name='google',
            price=Decimal('9.53')
        )

        self.browser.get(self.live_server_url)

        # the user sees the project on screen
        self.assertEquals(
            self.browser.find_element_by_class_name('stock_name').text,
            'google'
        )