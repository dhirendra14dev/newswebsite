from django.db import models
from datetime import datetime

class Subscribe(models.Model):
  email = models.CharField(max_length=200)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)

  


