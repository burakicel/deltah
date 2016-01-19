from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime

class Enterprise(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=25, default="Unnamed store")
    def __str__(self):
        return '{}'.format(self.name)

class Customer(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return '{}'.format(self.user.username)

class Offer(models.Model):
    name = models.CharField(max_length=50, default="Unnamed offer")
    enterprise = models.ForeignKey('Enterprise');
    quantity = models.IntegerField();
    product_title = models.TextField();
    reward = models.TextField();
    participants = models.IntegerField(default=0);
    total_bought = models.IntegerField(default=0);
    def __str__(self):
        return '{}'.format(self.name)

class Transaction(models.Model):
    enterprise = models.ForeignKey('Enterprise', related_name='enterprise');
    price = models.DecimalField(decimal_places=2, max_digits=20);
    offer = models.ForeignKey('Offer');
    customer = models.ForeignKey('Customer', related_name='customer')
    date = models.DateTimeField(auto_now_add=True, blank=True)