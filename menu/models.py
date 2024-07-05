from django.db import models

# Create your models here.
class Coffe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
