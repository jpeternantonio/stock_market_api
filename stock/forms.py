from django import forms
from .models import Purchased

GEEKS_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 
class PurchasedForm(forms.Form):

    stock = forms.CharField()
    price = forms.FloatField()
    share = forms.ChoiceField(choices=GEEKS_CHOICES)

class BuyForm(forms.ModelForm):
    class Meta:
        model = Purchased

        fields=['share', 'price']