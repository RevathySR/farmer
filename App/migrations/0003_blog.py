# Generated by Django 3.2.7 on 2022-04-17 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_crop'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=500)),
                ('description', models.CharField(default='none', max_length=50000)),
                ('image', models.ImageField(upload_to='blog')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 4, 17, 5, 42, 16, 754098))),
            ],
        ),
    ]
