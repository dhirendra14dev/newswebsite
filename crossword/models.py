from django.db import models

class Crossword(models.Model):
  
  word = models.CharField(max_length=20, blank=True)
  clue = models.CharField(max_length=200, blank=True)
  start_position = models.IntegerField(blank=True)
  start_position_x = models.IntegerField(blank=True, default= 0)
  start_position_y = models.IntegerField(blank=True, default= 0)
  is_across = models.BooleanField(default=True)
  
class Crosswordcheck(models.Model):
  
  result = models.TextField(blank=True)
  name = models.CharField(max_length=200 ,default='')
  email = models.CharField(max_length=200)
  subscribe_yes = models.BooleanField(default=True)
  contest_result = models.BooleanField(default=True)