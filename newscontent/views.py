from django.shortcuts import render, get_object_or_404
from .models import Newscontent

def archives(request):
  stories= Newscontent.objects.all()
  
  
  context = {
    'stories': stories
  }
  return render(request, 'newscontent/archives.html',context)


def newscontent(request,newscontent_id):
  newscontent = get_object_or_404(Newscontent, pk=newscontent_id)
  context = {
    'newscontent': newscontent
  }
  return render(request, 'newscontent/newscontent.html',context)

