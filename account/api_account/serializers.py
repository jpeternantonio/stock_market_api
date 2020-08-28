from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['id', 'name', 'balance']

