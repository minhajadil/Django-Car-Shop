from django.db import models
from cars.models import Car
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    Comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
        
