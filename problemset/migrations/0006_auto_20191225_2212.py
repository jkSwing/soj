# Generated by Django 2.1.14 on 2019-12-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemset', '0005_auto_20191216_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='lang',
            field=models.SmallIntegerField(choices=[(1, 'GXX'), (2, 'GCC'), (3, 'Java'), (4, 'CPY'), (5, 'Go'), (6, 'JavaScript')]),
        ),
    ]
