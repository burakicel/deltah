# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20160117_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.date(2016, 1, 17)),
        ),
    ]
