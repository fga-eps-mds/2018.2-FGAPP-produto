from django.db import models

class ProductList(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to="product_list/photos/", null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
