from django.db import models

# Create your models here.
class Jamboard(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class File(models.Model):
    file = models.FileField(upload_to='static/files/')
    jamboard = models.ForeignKey(Jamboard, on_delete=models.CASCADE,related_name='files')
    def __str__(self):
        return self.file.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='static/images/')
    jamboard = models.ForeignKey(Jamboard, on_delete=models.CASCADE,related_name='images')
    def __str__(self):
        return self.image.name