from django.db import models

# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=150)
    date= models.DateField() 
    location = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    declassified = models.BooleanField(default=True)
    foia = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name