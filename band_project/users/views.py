from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request , 'users/home.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request , 'Username Taken')
                print("Username taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request , 'email Taken')
                print("email taken")
                return redirect('register')

  

            else:    

                user = User.objects.create_user(username=username , password=password1 , email=email , first_name =first_name , last_name =last_name)
                user.save();
                messages.success(request , f'Your account has been created.You can log in now !')

        else:
            print('password not matching')
            return redirect('register')


        return redirect('/')

    return render(request , 'register.html')