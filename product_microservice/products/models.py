from django.db import models

# Create your models here.
class Product(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    fk_vendor = models.IntegerField(default= '0')
    name = models.TextField()
    price = models.FloatField(default= '0.0')
    photo = models.TextField()
    description = models.TextField()

    class Meta:
        ordering = ('created',)
