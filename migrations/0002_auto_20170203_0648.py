# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssrd_people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontranslation',
            name='function',
            field=models.CharField(blank=True, default='', verbose_name='title', max_length=255),
        ),
    ]
