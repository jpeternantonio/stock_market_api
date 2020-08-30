from django.urls import path, include
from . import views

app_name = 'stock'

urlpatterns = [
    path('stocks/',views.StockListView.as_view(), name='stock_list'),
    path('stocks/<pk>/', views.StockDetailView.as_view(), name='stock_detail'),
    path('users/',views.UserListView.as_view(), name='user_list'),
    path('users/<pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('stock/', views.StocksAddView.as_view(), name='stock_add'),
    path('purchased/',views.PurchasedListView.as_view(), name='purchased_list'),
    path('purchased/<pk>/', views.PurchasedDetailView.as_view(), name='purchased_detail'),
    path('buy/', views.PurchasedAddView.as_view(), name='buy'),
    path('sell/', views.SellView.as_view(), name='sell'),

]