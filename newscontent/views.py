from django.shortcuts import render,get_object_or_404
from .models import Newscontent

def archives(request):
  stories= Newscontent.objects.all()
  # stories.order_by("-published_date")
  print(stories)
  context = {
    'stories': stories
  }
  return render(request, 'newscontent/archives.html',context)


def newscontent(request,newscontent_id):
  newscontent = get_object_or_404(Newscontent, pk=newscontent_id)
  
  hyperlinked_text = newscontent.content.replace(newscontent.word1,"<a href={0} target={1}>{2}</a>".format(newscontent.link1,"_blank", newscontent.word1))
  hyperlinked_text = hyperlinked_text.replace(newscontent.word2,"<a href={0} target={1}>{2}</a>".format(newscontent.link2,"_blank", newscontent.word2))

  context = {
    'hyperlinked_text': hyperlinked_text ,
    'newscontent': newscontent
  }
  return render(request, 'newscontent/newscontent.html',context)

