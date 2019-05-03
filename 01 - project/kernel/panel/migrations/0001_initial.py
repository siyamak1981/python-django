# Generated by Django 2.1.4 on 2019-05-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrcingTabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PricingTabelAttrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PricingTabelLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('severity', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='prcingtabel',
            name='attrs',
            field=models.ManyToManyField(to='panel.PricingTabelAttrs'),
        ),
        migrations.AddField(
            model_name='prcingtabel',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabel', to='panel.PricingTabelLevel'),
        ),
    ]
