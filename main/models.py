from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('jersey', 'Jersey'),
        ('socks', 'Socks'),
        ('shin guard', 'Shin Guard'),
        ('cleat', 'Cleat'),
        ('ball', 'Ball'),
        ('hand gloves', 'Hand Gloves')
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField()
    brand = models.CharField(max_length=50, default='Unknown')
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name