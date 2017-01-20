# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0009_remove_website_template'),
        ('dbtemplates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='template',
            name='website',
            field=models.ForeignKey(related_name='templates', to='websites.Website', null=True),
        ),
    ]
