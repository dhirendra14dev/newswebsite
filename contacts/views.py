from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    

    contact = Contact(name=name, email=email, message=message)

    contact.save()

    messages.success(request, "Thanks for getting in touch! We'll get back soon.")
    return redirect('/contactus')
  
