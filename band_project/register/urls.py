from django import views
from django.urls import  path
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register_user', views.register_user , name ="register"),


]

