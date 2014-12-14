# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_answer_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='last_activity_date',
            field=models.DateTimeField(verbose_name='last activity date', null=True),
            preserve_default=True,
        ),
    ]
