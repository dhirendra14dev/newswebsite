from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Storytitle


def storytitle(request):
  return render(request, 'pages/storytitle.html')

def storytitle_submit(request):
  if request.method == 'POST':
    title = request.POST['title']
    name = request.POST['name']
    email = request.POST['email']
    
    wish_to_subscribe = request.POST.get('wish_to_subscribe', False )
   
    if wish_to_subscribe == 'on':
      wish_to_subscribe = True
    if wish_to_subscribe == 'off':
      wish_to_subscribe = False
   


    storytitle = Storytitle(title=title, name=name, email=email, wish_to_subscribe=wish_to_subscribe)

    storytitle.save()

    return render(request, 'pages/contestsubmit.html')
  
