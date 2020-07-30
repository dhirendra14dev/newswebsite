from django.shortcuts import render,get_object_or_404
from .models import Latest
from datetime import datetime

def latestnews(request):

  latestnews= Latest.objects.all().filter(is_published=True)
 
  
  context = {
    'latestnews':latestnews,
  }
  return render(request, 'pages/latestpage.html', context)