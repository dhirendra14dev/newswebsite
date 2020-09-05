from django.shortcuts import render,get_object_or_404
from newscontent.models import Newscontent
import random
def subscribe(request):
  return render(request, 'pages/subscribe.html')

def index(request):
  stories_all= Newscontent.objects.all().filter(is_published=True)
  stories_id_list = stories_all.values_list('id', flat=True)
  random_id_list = random.sample(list(stories_id_list), 6)
  random_stories = stories_all.filter(id__in = random_id_list)
  context = {
    'random_stories': random_stories,
  }
  return render(request, 'pages/index.html', context)


  

def about(request):
  return render(request, 'pages/about.html')

def contactus(request):
  return render(request, 'pages/contact.html')

def latest(request):
  return render(request, 'pages/latest.html')







