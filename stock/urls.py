from django.urls import path
from . import views

#app_name = 'stock'

urlpatterns = [
    path('', views.StockListView.as_view(), name='stock-list'),
    path('buy/<int:pk>', views.buy_stock, name='buy_stock'),
    path('buy_done', views.buy_done, name='buy_done'),
    path('buy_history', views.buy_history, name='buy_history'),
    path('sell/<int:pk>', views.sell, name='sell'),
    path('sell_done', views.sell_done, name='sell_done'),
]