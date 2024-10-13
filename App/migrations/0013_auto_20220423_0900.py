# Generated by Django 3.2.7 on 2022-04-23 15:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0012_auto_20220423_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 9, 0, 24, 429227)),
        ),
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 9, 0, 24, 429227)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 9, 0, 24, 429227)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 9, 0, 24, 429227)),
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=500)),
                ('image', models.ImageField(default='default.jpg', upload_to='products')),
                ('contact', models.CharField(default='none', max_length=500)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 4, 23, 9, 0, 24, 430227))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
