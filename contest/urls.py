from django.urls import path
from . import views

urlpatterns = [
  
  path('storytitle', views.storytitle, name='storytitle'),
  path('storytitle_submit', views.storytitle_submit, name='storytitle_submit'),
  
  
]