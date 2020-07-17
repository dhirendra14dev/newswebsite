from django.shortcuts import render,get_object_or_404
from .models import Newscontent

def archives(request):
  stories= Newscontent.objects.all()
  
  
  context = {
    'stories': stories
  }
  return render(request, 'newscontent/archives.html',context)


def newscontent(request,newscontent_id):
  newscontent = get_object_or_404(Newscontent, pk=newscontent_id)
  print(newscontent.published_date)
  hyperlinked_text = newscontent.content.replace(newscontent.word,"<a href={0} target={1}>{2}</a>".format(newscontent.link,"_blank", newscontent.word))
  context = {
    'hyperlinked_text': hyperlinked_text ,
    'newscontent': newscontent
  }
  return render(request, 'newscontent/newscontent.html',context)

