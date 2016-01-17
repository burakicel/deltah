from django.contrib import admin
from .models import Enterprise, Customer, Offer

# Register your models here.
class EnterpriseAdmin(admin.ModelAdmin):
       list_display = ['user']

class CustomerAdmin(admin.ModelAdmin):
       list_display = ['user']

class OfferAdmin(admin.ModelAdmin):
       list_display = ['name','enterprise','quantity','product_title','reward','participants','total_bought']

admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Offer,OfferAdmin)