from django.db import models

# Create your models here.
class Url(models.Model):
  origin_url = models.TextField()
  short_url = models.CharField(max_length=25, unique=True)
  
  def __str__(self):
    return self.origin_url