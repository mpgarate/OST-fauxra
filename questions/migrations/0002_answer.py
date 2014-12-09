# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(verbose_name=b'date published')),
                ('question', models.ForeignKey(to='questions.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
