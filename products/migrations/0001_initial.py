# Generated by Django 3.2.13 on 2022-06-09 15:41

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('product_name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('hoppyness', models.IntegerField(blank=True, null=True)),
                ('bitterness', models.IntegerField(blank=True, null=True)),
                ('maltyness', models.IntegerField(blank=True, null=True)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ibu', models.IntegerField(blank=True, null=True)),
                ('og', models.DecimalField(decimal_places=4, max_digits=6)),
                ('hops', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=254, null=True), default=list, size=None)),
                ('malts', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=254, null=True), default=list, size=None)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_stock', models.IntegerField(blank=True, null=True)),
                ('product_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('product_banner_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_banner_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.style')),
            ],
        ),
    ]
