from django.db import models
from datetime import datetime


class Newscontent(models.Model):
  title = models.CharField(max_length=200)
  published_date = models.DateField(blank=True)
  content = models.TextField()
  image = models.ImageField(blank=True)

  def __str__(self):
    return self.title
