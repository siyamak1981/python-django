# Generated by Django 2.1.2 on 2019-05-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20190528_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sku',
            field=models.CharField(default='vaoJv7bMkB2OMhD8RoIhcg', editable=False, max_length=128, primary_key=True, serialize=False),
        ),
    ]
