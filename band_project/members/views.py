from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
# Create your views here.

def login_user(request ):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged In!'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging In - Please Try Again...'))
            return redirect('login')
	
    else:
        return render(request , 'authenticate/login.html' , {})

