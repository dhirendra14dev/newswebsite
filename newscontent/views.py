from django.shortcuts import render,get_object_or_404
from .models import Newscontent
from datetime import datetime

month_dict = {
    'January':1,
    'February':2,
    'March':3,
    'April':4,
    'May':5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'Decemebr':12,
  }

def latest(request):

  return render(request, 'newscontent/latest.html')

def search(request):

  month = int(request.GET['month'])
  year = request.GET['year']
  stories_selected_month = Newscontent.objects.filter(published_date__year = year).filter(published_date__month=month).filter(is_published=True)

  length_query = len(stories_selected_month)
 
  
  context = {
    'month': month,
    'year':year,
    'stories_selected_month':stories_selected_month,
    'length_query':length_query,
    'month_dict':month_dict,
  }
  return render(request, 'newscontent/search.html', context)

def archives(request):
  
  first_story = Newscontent.objects.order_by('published_date').first()
  
  
  last_story = Newscontent.objects.order_by('published_date').last()
  print(last_story.published_date.day)
  print(last_story.title)
  print(last_story.published_date < datetime.now().date())
  
  stories= Newscontent.objects.filter(published_date__year = datetime.now().year).filter(published_date__month=datetime.now().month).filter(is_published=True)
  
  stories_all= Newscontent.objects.all().filter(is_published=True)
  
  def get_correct_month():
    
      if last_story.published_date.month == datetime.now().month:
        correct_month = last_story.published_date.month
        return correct_month
      else:
        correct_month = last_story.published_date.month - 1
        return correct_month 
    
  correct_month = get_correct_month()
 

  context = {
    'stories': stories,
    'first_story':first_story,
    'last_story':last_story,
    'correct_month':correct_month,
    'month_dict':month_dict,
    
  }

  return render(request, 'newscontent/archives.html',context)


def newscontent(request,newscontent_id):
  newscontent = get_object_or_404(Newscontent, pk=newscontent_id)
  
  if newscontent.word2 != '':
    hyperlinked_text = newscontent.content.replace(newscontent.word1,"<a href={0} target={1}>{2}</a>".format(newscontent.link1,"_blank", newscontent.word1))

    hyperlinked_text = hyperlinked_text.replace(newscontent.word2,"<a href={0} target={1}>{2}</a>".format(newscontent.link2,"_blank", newscontent.word2))
  elif newscontent.word1 != '':
    hyperlinked_text = newscontent.content.replace(newscontent.word1,"<a href={0} target={1}>{2}</a>".format(newscontent.link1,"_blank", newscontent.word1))
  else:
    hyperlinked_text = newscontent.content


  context = {
    'hyperlinked_text': hyperlinked_text ,
    'newscontent': newscontent
  }
  return render(request, 'newscontent/newscontent.html',context)

