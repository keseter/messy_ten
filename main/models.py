from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('jerseys', 'Jerseys'),
        ('shorts', 'Shorts'),
        ('training_wear', 'Training Wear'),
        ('footwear', 'Footwear'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('collectibles', 'Collectibles'),
        ('fan_gear', 'Fan Gear'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jerseys')
    is_featured = models.BooleanField(default=False)

    #
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)       

    # optional 
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    total_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.stock > 20

#test