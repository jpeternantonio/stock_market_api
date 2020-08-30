from django import forms
from .models import Purchased



# For future use after finishing needed requirements

"""
CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

class PurchasedForm(forms.Form):

    stock = forms.CharField()
    price = forms.FloatField()
    share = forms.ChoiceField(choices=CHOICES)

class BuyForm(forms.ModelForm):
    class Meta:
        model = Purchased

        fields=['share', 'price']

"""