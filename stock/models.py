from django.db import models
from account.models import User
from django.urls import reverse


class Stocks(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Stocks'


class Purchased(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        db_index=True,
    )
    stock = models.ForeignKey(
        Stocks, on_delete=models.CASCADE
    )
    share = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


    # Just in case this will be needed
    # def invest(self):
    #     return self.share * self.price

 