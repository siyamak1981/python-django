# Generated by Django 2.1.2 on 2019-05-30 10:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 30, 10, 15, 2, 26754, tzinfo=utc)),
        ),
    ]
