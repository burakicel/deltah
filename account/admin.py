from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
       list_display = ['user', 'is_enterprise', 'is_customer']

admin.site.register(Client, ClientAdmin)
