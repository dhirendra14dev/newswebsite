from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Latest(models.Model):
  title = models.CharField(max_length=200)
  published_date = models.DateField(blank=True)
  is_published = models.BooleanField(default=True)
  abstract = RichTextField(blank=True, null=True)
  #Section1#
  main_heading1 = models.CharField(max_length=200)
  image1_1 = models.ImageField(upload_to='photos', blank=True)
  image_credits1_1 = models.CharField(max_length=200, blank=True)
  title1_1 = models.CharField(max_length=200, blank=True)
  content1_1 = RichTextField(blank=True, null=True)
  s_link1_1_1 = models.TextField(blank=True)
  s_link1_1_2 = models.TextField(blank=True)

  image1_2 = models.ImageField(upload_to='photos', blank=True)
  image_credits1_2 = models.CharField(max_length=200, blank=True)
  title1_2 = models.CharField(max_length=200, blank=True)
  content1_2 = RichTextField(blank=True, null=True)
  s_link1_2_1 = models.TextField(blank=True)
  s_link1_2_2 = models.TextField(blank=True)

  image1_3 = models.ImageField(upload_to='photos', blank=True)
  image_credits1_3 = models.CharField(max_length=200, blank=True)
  title1_3 = models.CharField(max_length=200, blank=True)
  content1_3 = RichTextField(blank=True, null=True)
  s_link1_3_1 = models.TextField(blank=True)
  s_link1_3_2 = models.TextField(blank=True)

  image1_4 = models.ImageField(upload_to='photos', blank=True)
  image_credits1_4 = models.CharField(max_length=200, blank=True)
  title1_4 = models.CharField(max_length=200, blank=True)
  content1_4 = RichTextField(blank=True, null=True)
  s_link1_4_1 = models.TextField(blank=True)
  s_link1_4_2 = models.TextField(blank=True)

  #Section2#
  main_heading2 = models.CharField(max_length=200)
  image2_1 = models.ImageField(upload_to='photos', blank=True)
  image_credits2_1 = models.CharField(max_length=200, blank=True)
  title2_1 = models.CharField(max_length=200, blank=True)
  content2_1 = RichTextField(blank=True, null=True)
  s_link2_1_1 = models.TextField(blank=True)
  s_link2_1_2 = models.TextField(blank=True)

  image2_2 = models.ImageField(upload_to='photos', blank=True)
  image_credits2_2 = models.CharField(max_length=200, blank=True)
  title2_2 = models.CharField(max_length=200, blank=True)
  content2_2 = RichTextField(blank=True, null=True)
  s_link2_2_1 = models.TextField(blank=True)
  s_link2_2_2 = models.TextField(blank=True)

  image2_3 = models.ImageField(upload_to='photos', blank=True)
  image_credits2_3 = models.CharField(max_length=200, blank=True)
  title2_3 = models.CharField(max_length=200, blank=True)
  content2_3 = RichTextField(blank=True, null=True)
  s_link2_3_1 = models.TextField(blank=True)
  s_link2_3_2 = models.TextField(blank=True)

  image2_4 = models.ImageField(upload_to='photos', blank=True)
  image_credits2_4 = models.CharField(max_length=200, blank=True)
  title2_4 = models.CharField(max_length=200, blank=True)
  content2_4 = RichTextField(blank=True, null=True)
  s_link2_4_1 = models.TextField(blank=True)
  s_link2_4_2 = models.TextField(blank=True)

  #Section3#
  main_heading3 = models.CharField(max_length=200)
  image3_1 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_1 = models.CharField(max_length=200, blank=True)
  title3_1 = models.CharField(max_length=200, blank=True)
  content3_1 = RichTextField(blank=True, null=True)
  s_link3_1_1 = models.TextField(blank=True)
  s_link3_1_2 = models.TextField(blank=True)

  image3_2 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_2 = models.CharField(max_length=200, blank=True)
  title3_2 = models.CharField(max_length=200, blank=True)
  content3_2 = RichTextField(blank=True, null=True)
  s_link3_2_1 = models.TextField(blank=True)
  s_link3_2_2 = models.TextField(blank=True)

  image3_3 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_3 = models.CharField(max_length=200, blank=True)
  title3_3 = models.CharField(max_length=200, blank=True)
  content3_3 = RichTextField(blank=True, null=True)
  s_link3_3_1 = models.TextField(blank=True)
  s_link3_3_2 = models.TextField(blank=True)

  image3_4 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_4 = models.CharField(max_length=200, blank=True)
  title3_4 = models.CharField(max_length=200, blank=True)
  content3_4 = RichTextField(blank=True, null=True)
  s_link3_4_1 = models.TextField(blank=True)
  s_link3_4_2 = models.TextField(blank=True)

  image3_5 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_5 = models.CharField(max_length=200, blank=True)
  title3_5 = models.CharField(max_length=200, blank=True)
  content3_5 = RichTextField(blank=True, null=True)
  s_link3_5_1 = models.TextField(blank=True)
  s_link3_5_2 = models.TextField(blank=True)

  image3_6 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_6 = models.CharField(max_length=200, blank=True)
  title3_6 = models.CharField(max_length=200, blank=True)
  content3_6 = RichTextField(blank=True, null=True)
  s_link3_6_1 = models.TextField(blank=True)
  s_link3_6_2 = models.TextField(blank=True)

  image3_7 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_7 = models.CharField(max_length=200, blank=True)
  title3_7 = models.CharField(max_length=200, blank=True)
  content3_7 = RichTextField(blank=True, null=True)
  s_link3_7_1 = models.TextField(blank=True)
  s_link3_7_2 = models.TextField(blank=True)

  image3_8 = models.ImageField(upload_to='photos', blank=True)
  image_credits3_8 = models.CharField(max_length=200, blank=True)
  title3_8 = models.CharField(max_length=200, blank=True)
  content3_8 = RichTextField(blank=True, null=True)
  s_link3_8_1 = models.TextField(blank=True)
  s_link3_8_2 = models.TextField(blank=True)
  
  
  #Section4#
  main_heading4 = models.CharField(max_length=200)
  
  content4_1 = RichTextField(blank=True, null=True)
  
  content4_2 = RichTextField(blank=True, null=True)
  
  content4_3 = RichTextField(blank=True, null=True)
  
  content4_4 = RichTextField(blank=True, null=True)

  content4_5 = RichTextField(blank=True, null=True)
  
#Section5#
  main_heading5 = models.CharField(max_length=200)
  title5_1 = models.CharField(max_length=200, blank=True)
  content5_1 = RichTextField(blank=True, null=True)
  title5_2 = models.CharField(max_length=200, blank=True)
  content5_2 = RichTextField(blank=True, null=True)
  title5_3 = models.CharField(max_length=200, blank=True)
  content5_3 = RichTextField(blank=True, null=True)
  title5_4 = models.CharField(max_length=200, blank=True)
  content5_4 = RichTextField(blank=True, null=True)
  title5_5 = models.CharField(max_length=200, blank=True)
  content5_5 = RichTextField(blank=True, null=True)
  
  
  
  def __str__(self):
    return self.title


