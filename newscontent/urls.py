from django.urls import path
from . import views

urlpatterns = [
  path('', views.archives, name='archives'),
  path('<int:newscontent_id>',views.newscontent, name='newscontent'),
]