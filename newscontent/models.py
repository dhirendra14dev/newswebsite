from django.db import models
from datetime import datetime


class Newscontent(models.Model):
  title = models.CharField(max_length=200)
  published_date = models.DateField(blank=True)
  content = models.TextField()
  word = models.CharField(max_length=200, blank=True)
  link = models.TextField(blank=True)
  image = models.ImageField(blank=True)


  def __str__(self):
    return self.title
