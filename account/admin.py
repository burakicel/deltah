from django.contrib import admin
from .models import Enterprise, Customer, Offer, Transaction

# Register your models here.
class EnterpriseAdmin(admin.ModelAdmin):
       list_display = ['user']

class CustomerAdmin(admin.ModelAdmin):
       list_display = ['user']

class OfferAdmin(admin.ModelAdmin):
       list_display = ['name','enterprise','quantity','product_title','reward','participants','total_bought']

class TransactionAdmin(admin.ModelAdmin):
       list_display = ['enterprise','price','offer','customer','date']

admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Transaction,TransactionAdmin)