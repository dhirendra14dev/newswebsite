from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscribe

def subscribe(request):
  if request.method == 'POST':
    
    email = request.POST['email']
  
    subscribe = Subscribe(email=email)

    subscribe.save()

    messages.success(request, 'We have got your message, will get back to you soon!')
    return redirect('/')
