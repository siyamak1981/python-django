# Generated by Django 2.1.2 on 2019-05-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190528_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sku',
            field=models.CharField(default='aLAKz5zpiJffNqxFUy5WVg', editable=False, max_length=128, primary_key=True, serialize=False),
        ),
    ]
