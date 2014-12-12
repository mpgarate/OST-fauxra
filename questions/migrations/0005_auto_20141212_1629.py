# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('questions', '0004_answer_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
