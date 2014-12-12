# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20141212_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date_updated',
            field=models.DateTimeField(verbose_name='date updated', null=True),
            preserve_default=True,
        ),
    ]
