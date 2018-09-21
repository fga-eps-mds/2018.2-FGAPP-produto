from django.db import models

# Create your models here.
class Product(models.Model):
    fk_vendor = models.IntegerField(default= '0')
    name = models.CharField()
    price = models.FloatField(default= '0.0')
    photo = models.CharField()
    description = models.TextField()

    class Meta:
        ordering = ('created',)
