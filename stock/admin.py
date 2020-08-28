from django.contrib import admin
from .models import Stocks

@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']