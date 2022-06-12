from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Style(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    style = models.ForeignKey('Style', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    description = models.TextField()
    descriptive_words = ArrayField(models.CharField(max_length=254, null=True, blank=True), default=list)
    color = models.IntegerField(null=True, blank=True)
    hoppyness = models.IntegerField(null=True, blank=True)
    bitterness = models.IntegerField(null=True, blank=True)
    maltyness = models.IntegerField(null=True, blank=True)
    percentage = models.DecimalField(max_digits=6, decimal_places=2)
    ibu = models.IntegerField(null=True, blank=True)
    og = models.DecimalField(max_digits=6, decimal_places=4)
    hops = ArrayField(models.CharField(max_length=254, null=True, blank=True), default=list)
    malts = ArrayField(models.CharField(max_length=254, null=True, blank=True), default=list)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    product_banner_url = models.URLField(max_length=1024, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)
    product_banner_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name
