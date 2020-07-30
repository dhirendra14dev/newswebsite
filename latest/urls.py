from django.urls import path
from . import views

urlpatterns = [
  path('', views.latestnews, name='latestnews'),
]