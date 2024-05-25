from django.urls import path  # import the path
from . import views;

urlpatterns = [  # this will used to specfiying the url pattrens
        path('', views.home, name = 'home'),
        path('add', views.add, name="add")
    
]