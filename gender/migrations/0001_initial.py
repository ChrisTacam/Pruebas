# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gender.models
import dj.choices.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', dj.choices.fields.ChoiceField(default=3, choices=gender.models.Gender)),
            ],
        ),
    ]
