from rest_framework import generics
from .serializers import StockSerializer, PurchasedSerializer, UserSerializer
from rest_framework import permissions, parsers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Stocks, Purchased
from account.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StockListView(generics.ListAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer

class StockDetailView(generics.RetrieveAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer

class PurchasedListView(generics.ListAPIView):
    queryset = Purchased.objects.all()
    serializer_class = PurchasedSerializer
    
class PurchasedDetailView(generics.RetrieveAPIView):
    queryset = Purchased.objects.all()
    serializer_class = PurchasedSerializer



class StocksAddView(APIView): # For superuser only
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (parsers.JSONParser,)

    def post(self, request, format=None):
        stock_name = request.data['name']
        stock_price = request.data['price']
        stock = Stocks(name=stock_name, price=stock_price)
        stock.save()
        return Response('stock added successfully')


class PurchasedAddView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (parsers.JSONParser,)

    def post(self, request, format=None):
      
        user_id = request.data['user_id']
        stock_id = request.data['stock_id']
        share = float(request.data['share'])
        price = float(request.data['price'])
        total = share * price
        user = User.objects.get(id=user_id)
        user_balance = user.balance
        user.balance -= total
        user.save()
        buy = Purchased(user_id=user_id, stock_id=stock_id, share=share, price=price)
        buy.save()
        return Response('purchased successfully')


class SellView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (parsers.JSONParser,)

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass
    
    def put(self, request, format=None):
        user_id = request.data['user_id']
        sell_id = request.data['id']
        share = float(request.data['share'])
        price = float(request.data['price'])
        total = share * price
        user = User.objects.get(id=user_id)
        user_balance = user.balance
        user.balance += total
        user.save()
        sell = Purchased.objects.get(id=sell_id)
        sell.share -= share
        sell.save()