# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('heartbeat_pts', models.TextField()),
                ('heartbeat_avg', models.FloatField()),
                ('mic_pts', models.TextField()),
                ('mic_avg', models.FloatField()),
                ('acc_watch_x_pts', models.TextField()),
                ('acc_watch_x_avg', models.FloatField()),
                ('acc_watch_y_pts', models.TextField()),
                ('acc_watch_y_avg', models.FloatField()),
                ('acc_watch_z_pts', models.TextField()),
                ('acc_watch_z_avg', models.FloatField()),
                ('acc_phone_x_pts', models.TextField()),
                ('acc_phone_x_avg', models.FloatField()),
                ('acc_phone_y_pts', models.TextField()),
                ('acc_phone_y_avg', models.FloatField()),
                ('acc_phone_z_pts', models.TextField()),
                ('acc_phone_z_avg', models.FloatField()),
                ('activity', models.IntegerField()),
                ('emotion', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
