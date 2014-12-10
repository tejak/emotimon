# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_emotimon', '0002_auto_20141124_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='user_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
