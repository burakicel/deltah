# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160117_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='name',
            field=models.CharField(default=b'Unnamed offer', max_length=50),
        ),
    ]
