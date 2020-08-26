from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscribe

def subscribe(request):
  if request.method == 'POST':
    
    email = request.POST['email']
  
    subscribe = Subscribe(email=email)

    subscribe.save()

    messages.success(request, 'Thank you for subscribing! Look out for R&I in your inbox on Saturday.')
    return redirect('/')
