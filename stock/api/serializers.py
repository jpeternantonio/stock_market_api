from rest_framework import serializers
from ..models import Stocks, Purchased
from account.models import User


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['id', 'name', 'price']


class PurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchased
        fields = ['id', 'user_id', 'stock_id', 'share', 'price']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'balance']