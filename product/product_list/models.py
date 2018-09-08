from django.db import models
from django.contrib.auth.models import User

class ProductList(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to="product_list/photos/", null=True, blank=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
