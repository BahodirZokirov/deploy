from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    RAM = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name