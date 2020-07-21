from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,"generator/home.html")

def password(request):
    
    charachters = list('')
    
    length = int(request.GET.get('kitna lamba?',0))
    
    if request.GET.get('letters'):
        charachters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    
    if request.GET.get('Uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('numbers'):
        charachters.extend(list('1234567890'))
     
    if request.GET.get('Special'):
        charachters.extend(list('!@#$%^&*+_-~?'))
    
    thepassword=''
    
    for x in range(length):
        thepassword += random.choice(charachters)
    
    return render(request,"generator/password.html",{'password':thepassword})

def about(request):
    return render(request,"generator/about.html")