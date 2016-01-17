from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User)
    is_enterprise = models.BooleanField(default=False);
    is_customer = models.BooleanField(default=True);

    def __str__(self):
        return 'Client for user {}'.format(self.user.username)