from django.urls import path  # import the path
from . import views;

urlpatterns = [  # this will used to specfiying the url pattrens
        path('', views.index, name = 'index'),
        # path("", views.index, name="about") 
]