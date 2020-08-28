from django import forms
from .models import Purchased

class PurchasedForm(forms.Form):
    model = Purchased
    fields = '__all__'