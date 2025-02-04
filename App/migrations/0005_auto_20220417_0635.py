# Generated by Django 3.2.7 on 2022-04-17 12:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0004_auto_20220417_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 6, 35, 13, 785774)),
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='none', max_length=10000000)),
                ('chat_between', models.CharField(default='none', max_length=10000000)),
                ('time', models.DateTimeField(default=datetime.datetime(2022, 4, 17, 6, 35, 13, 785774))),
                ('from_u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_u', to=settings.AUTH_USER_MODEL)),
                ('sent_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_by', to=settings.AUTH_USER_MODEL)),
                ('to_u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_u', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
