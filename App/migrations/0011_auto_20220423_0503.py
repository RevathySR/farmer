# Generated by Django 3.2.7 on 2022-04-23 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20220423_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contact',
            field=models.CharField(default='none', max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 5, 3, 0, 474028)),
        ),
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 5, 3, 0, 474028)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 5, 3, 0, 474028)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 5, 3, 0, 475028)),
        ),
    ]
