# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20141212_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date_updated',
            field=models.DateTimeField(verbose_name='date updated', null=True),
            preserve_default=True,
        ),
    ]
