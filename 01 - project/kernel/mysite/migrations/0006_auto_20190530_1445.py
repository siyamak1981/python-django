# Generated by Django 2.1.2 on 2019-05-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20190529_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sku',
            field=models.CharField(default='gtRjF1y5gl1yew8WDk_aMg', editable=False, max_length=128, primary_key=True, serialize=False),
        ),
    ]
