from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class OfferForm(forms.Form):
	name = forms.CharField()
	quantity = forms.IntegerField()
	product_title = forms.CharField()
	reward = forms.CharField()
