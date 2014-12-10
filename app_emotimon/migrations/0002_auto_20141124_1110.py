# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_emotimon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='acc_phone_x_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_phone_x_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_phone_y_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_phone_y_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_phone_z_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_phone_z_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_watch_x_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_watch_x_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_watch_y_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_watch_y_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_watch_z_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='acc_watch_z_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='activity',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='emotion',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='heartbeat_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='heartbeat_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='mic_avg',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='mic_pts',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
