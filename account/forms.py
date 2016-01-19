from django import forms
from .models import Offer, Customer

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class OfferForm(forms.Form):
	name = forms.CharField()
	quantity = forms.IntegerField()
	product_title = forms.CharField()
	reward = forms.CharField()

class TransactionForm(forms.Form):
	price = forms.DecimalField()
	offer = forms.ModelChoiceField(queryset=Offer.objects.all())
	customer = forms.ModelChoiceField(queryset=Customer.objects.all())