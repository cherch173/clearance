from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

REPORTS = (
    ('I', 'Internet'),
    ('N', 'Newspaper'),
    ('P', 'Press Conference'),
    ('T', 'Television'),
)

class Testimony(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateField()
  location = models.CharField()
  comments = models.CharField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('testimonies_detail', kwargs={'pk': self.id})

# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=150)
    date= models.DateField() 
    location = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    #declassified = models.BooleanField(default=True)
    foia = models.CharField(max_length=300)
    testimonies = models.ManyToManyField(Testimony)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.id})'

    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'case_id': self.id})
    

class Reporting(models.Model):
    date = models.DateField('Date Published')
    report = models.CharField(
        max_length=1,
        choices=REPORTS,
        default=REPORTS[0][0]
    )
    case = models.ForeignKey(
        Case, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_report_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

    
class Photo(models.Model):
     url = models.CharField(max_length=200)
     case = models.ForeignKey(Case, on_delete=models.CASCADE)

     def __str__(self):
        return f"Photo for case_id: {self.case_id} @{self.url}"