from django.db import models
import uuid

class Product(models.Model):
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
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES, # The UI bar
        default='jerseys'
    )
    is_featured = models.BooleanField(default=False)
#todo category
    # ooptinal
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    total_sold = models.IntegerField(default=0)  

    def __str__(self):
        return self.name
