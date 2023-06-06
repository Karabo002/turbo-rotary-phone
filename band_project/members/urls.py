from django import views
from django.urls import  path
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login_user', views.login_user , name ="login"),


]
