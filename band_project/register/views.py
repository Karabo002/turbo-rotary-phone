from imaplib import _Authenticator
from telnetlib import AUTHENTICATION
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm
# Create your views here.

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.Post)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.changed_data['password1']
            # user = AUTHENTICATION(username=username , password=password) 
            # login(request , user)  

        return redirect("/home")
    else:
        form=RegisterForm()
    
    return render(response , "register/register.html" , {"form":form,})
