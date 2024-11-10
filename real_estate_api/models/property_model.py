import uuid
from django.db import models

class Property(models.Model):
    uid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    property_name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    property_image = models.ImageField(null=True)
    no_of_rooms = models.IntegerField(null=True)
    no_of_bathroom = models.IntegerField(null=True)
    no_of_grid = models.IntegerField(null=True)
    no_of_garage = models.IntegerField(null=True)
    posted_date = models.DateField(null = True)
    price = models.IntegerField(null=True)
    price_per_sqm = models.IntegerField(null=True)
    features = models.TextField(null=True)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Property'
        
    def __str__(self):
        return self.property_name
    

