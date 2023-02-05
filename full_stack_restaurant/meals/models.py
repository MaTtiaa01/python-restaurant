from django.db import models

# Create your models here.

class Meal(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    
    # define a function to read the db items with thei name
    def __str__(self):
        return self.name