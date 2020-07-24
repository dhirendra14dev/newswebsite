from django.urls import path
from . import views

urlpatterns = [
  path('', views.archives, name='archives'),
  path('search', views.search, name='search'),
  path('<int:newscontent_id>',views.newscontent, name='newscontent'),
]