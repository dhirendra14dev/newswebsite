from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Newscontent(models.Model):
  title = models.CharField(max_length=200)
  published_date = models.DateField(blank=True)
  # content = models.TextField()
  content = RichTextField(blank=True, null=True)
  is_published = models.BooleanField(default=True)
  word1 = models.CharField(max_length=200, blank=True)
  link1 = models.TextField(blank=True)
  word2 = models.CharField(max_length=200, blank=True)
  link2 = models.TextField(blank=True)
  word3 = models.CharField(max_length=200, blank=True)
  link3 = models.TextField(blank=True)
  s_link1 = models.TextField(blank=True)
  s_link2 = models.TextField(blank=True)
  s_link3 = models.TextField(blank=True)
  s_link4 = models.TextField(blank=True)
  image = models.ImageField(blank=True)


  def __str__(self):
    return self.title