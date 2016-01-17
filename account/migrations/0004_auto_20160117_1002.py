# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_enterprise_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='name',
            field=models.CharField(default=b'Unnamed store', max_length=25),
        ),
    ]
