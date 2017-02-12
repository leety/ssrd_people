# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ssrd_people', '0002_auto_20170203_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontranslation',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(verbose_name='Bio', blank=True, default=''),
        ),
    ]
