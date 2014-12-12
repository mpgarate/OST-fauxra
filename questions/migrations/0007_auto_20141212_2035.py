# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_question_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', blank=True, through='taggit.TaggedItem'),
            preserve_default=True,
        ),
    ]
