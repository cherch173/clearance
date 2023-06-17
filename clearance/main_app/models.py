from django.db import models

from django.urls import reverse

# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=150)
    date= models.DateField() 
    location = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    declassified = models.BooleanField(default=True)
    foia = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.name} ({self.id})'

    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'case_id': self.id})