from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    # ooptinal
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    total_sold = models.IntegerField(default=0)  

    def __str__(self):
        return self.name
