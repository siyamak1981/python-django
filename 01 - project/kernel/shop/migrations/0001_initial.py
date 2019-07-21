# Generated by Django 2.1.2 on 2019-05-28 20:45

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AttrValues',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('fk_attr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shop.Attributes')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='must be unique', max_length=128, unique_for_month='published_at')),
                ('slug', models.CharField(max_length=128, unique_for_month='published_at')),
                ('banner', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('banner1', models.ImageField(blank=True, upload_to='slider1/%Y/%m/%d')),
                ('banner2', models.ImageField(blank=True, upload_to='slider2/%Y/%m/%d')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('summary', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, default='0.0', max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.IntegerField(choices=[(0, 'Small'), (1, 'Xsmall'), (2, 'Large'), (3, 'Xlarge'), (4, 'Xxlarge')], default=0)),
                ('color', models.CharField(choices=[('RED', 'red'), ('WHITE', 'white'), ('BLUE', 'blue')], default='RED', max_length=5)),
                ('published_at', models.DateTimeField(default=datetime.datetime(2019, 5, 28, 20, 45, 29, 433254, tzinfo=utc))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['-published_at', 'name'],
                'get_latest_by': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shop.Product')),
            ],
            options={
                'verbose_name': 'product-type',
                'verbose_name_plural': 'product-types',
            },
        ),
        migrations.CreateModel(
            name='ProductTypeAttr',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fk_product_attr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shop.Attributes')),
                ('fk_product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shop.ProductType')),
            ],
        ),
        migrations.AddField(
            model_name='attributes',
            name='productattrvalue',
            field=models.ManyToManyField(related_name='attrvalue', to='shop.Product'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]