from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.TextField()
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'