from django.urls import path  # import the path
from . import views;

urlpatterns = [  # this will used to specfiying the url pattrens
        path('register', views.register, name = 'register'),
        path('login', views.login, name = 'login'),
        path('logout', views.logout, name = 'logout'),
        
       
]