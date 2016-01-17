# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160117_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='name',
            field=models.CharField(default=b"None's store", max_length=25),
        ),
    ]
