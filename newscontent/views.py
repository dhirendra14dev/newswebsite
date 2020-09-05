from django.shortcuts import render,get_object_or_404
from .models import Newscontent
from datetime import datetime
from taggit.models import Tag

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
quotes_dict = {
    'womens-issues':'<em>Feminism is the radical notion that women are people.\n - Marie Shear</em>',
    'human-rights':'<em>The rights of every man are diminished when the rights of one man are threatened.\n - John F. Kennedy</em>',
    'preserving-the-planet':'<em>We are the first generation to feel the effect of climate change and the last generation who can do something about it.\n - Barack Obama</em>',
    'innovation':'<em>Any sufficiently advanced technology is equivalent to magic.\n - Arthur C. Clarke</em>',
     'animal-rights':'<em>Humanity\'s true moral test, its fundamental test ... consists of its attitude towards those who are at its mercy: animals.\n - Milan Kundera</em>',
      'inspiring-and-uplifting':'<em>Life isn\'t about finding yourself. Life is about creating yourself.\n - George Bernard Shaw</em>',
       'arts-and-entertainment':'<em>The purpose of art is washing the dust of daily life off our souls.\n - Pablo Picasso</em>',
        'global-affairs':'<em>During times of universal deceit, telling the truth becomes a revolutionary act.\n - George Orwell</em>',
  }
def storiesbytopic(request,tag_slug=None):
  stories_all= Newscontent.objects.all().filter(is_published=True)
  tag = get_object_or_404(Tag, slug=tag_slug)
  storiesbytopic = stories_all.filter(tags__in=[tag])
  image_path = "./images/{0}.jpg".format(tag)
  
  tag_slug = tag.slug
  context = {
    'storiesbytopic': storiesbytopic,
    'tag':tag,
    'tag_slug':tag_slug,
    'quotes_dict':quotes_dict,
    'image_path':image_path,
  }
  return render(request, 'newscontent/tagstory.html', context)



def search(request):

  month = int(request.GET['month'])
  year = request.GET['year']
  stories_selected_month = Newscontent.objects.filter(published_date__year = year).filter(published_date__month=month).filter(is_published=True)

  length_query = len(stories_selected_month)
 
  first_month_of_year = Newscontent.objects.filter(published_date__year = datetime.now().year).order_by('published_date').first().published_date.month
  
  last_month_of_year = Newscontent.objects.filter(published_date__year = datetime.now().year).order_by('published_date').last().published_date.month

  context = {
    'month': month,
    'year':year,
    'stories_selected_month':stories_selected_month,
    'length_query':length_query,
    'month_dict':month_dict,
    'first_month_of_year':first_month_of_year,
    'last_month_of_year': last_month_of_year,
  }
  return render(request, 'newscontent/search.html', context)

def archives(request):

  
  first_story = Newscontent.objects.order_by('published_date').first()
  
  
  last_story = Newscontent.objects.order_by('published_date').filter(is_published=True).last()

  first_month_of_year = Newscontent.objects.filter(published_date__year = datetime.now().year).order_by('published_date').first().published_date.month
 
  last_month_of_year = Newscontent.objects.filter(published_date__year = datetime.now().year).order_by('published_date').last().published_date.month

  stories= Newscontent.objects.filter(published_date__year = datetime.now().year).filter(published_date__month=datetime.now().month).filter(is_published=True)
  
  stories_all= Newscontent.objects.all().filter(is_published=True)
  
  def get_correct_month():
    
      if last_story.published_date.month == datetime.now().month:
        correct_month = last_story.published_date.month
        return correct_month
      else:
        correct_month = datetime.now().month - 1
        return correct_month 
    
  correct_month = get_correct_month()
  stories= Newscontent.objects.filter(published_date__year = datetime.now().year).filter(published_date__month=correct_month).filter(is_published=True)
  context = {
    'stories': stories,
    'first_story':first_story,
    'last_story':last_story,
    'correct_month':correct_month,
    'month_dict':month_dict,
    'first_month_of_year':first_month_of_year,
    'last_month_of_year': last_month_of_year,
    
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

