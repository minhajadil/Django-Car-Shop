from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'



class Car(models.Model):
    image = models.ImageField(upload_to='cars/media/uploads/')
    name = models.CharField(max_length=120)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.BigIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name}'

User.add_to_class('bought_cars', models.ManyToManyField(Car, blank=True))

    