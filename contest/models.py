from django.db import models

class Storytitle(models.Model):
  
  title = models.CharField(max_length=200, blank=True)
  name = models.CharField(max_length=200, blank=True)
  email = models.CharField(max_length=200, blank=True)
  wish_to_subscribe = models.BooleanField(default=True)
  
  
