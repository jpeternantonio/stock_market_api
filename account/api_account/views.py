from rest_framework import generics
from .serializers import StockSerializer, PurchasedSerializer
from rest_framework import permissions, parsers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StockListView(generics.ListAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer

class StockDetailView(generics.RetrieveAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer
