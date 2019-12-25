# Generated by Django 2.1.14 on 2019-12-25 14:14

import common.consts
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20191218_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='lang',
            field=models.SmallIntegerField(choices=[(1, 'GXX'), (2, 'GCC'), (3, 'Java'), (4, 'CPY'), (5, 'Go'), (6, 'JavaScript')]),
        ),
        migrations.AlterField(
            model_name='submission',
            name='outputs',
            field=django_mysql.models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.SmallIntegerField(choices=[(-1, 'PENDING'), (0, 'AC'), (1, 'PE'), (2, 'TLE'), (3, 'MLE'), (4, 'WA'), (5, 'RE'), (6, 'OLE'), (7, 'CE'), (8, 'SE')], default=common.consts.VerdictResult(-1)),
        ),
    ]
