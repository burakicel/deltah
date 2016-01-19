# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_offer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='Customer',
            new_name='customer',
        ),
    ]
