from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    skills = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
