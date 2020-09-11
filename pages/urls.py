from django.urls import path
from . import views

urlpatterns = [
  path('subscribe',views.subscribe, name='subscribe'),
  path('about',views.about, name='about'),
  path('contactus',views.contactus, name='contactus'),
  path('latest',views.latest, name='latest'),
  path('contests',views.contests, name='contests'),
  path('',views.index, name='index'),
]