from django.shortcuts import render
from . models import Band
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request , 'about.html')

def band(request):
    bands=Band.objects.all()
    return render(request , 'band.html' , {'bands' : bands})


