from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.
def home(request):
    return render(request, "home.html",{'name':"madhukumar"}); #rendering the template it might be html contenet we can use this way to run  we methion the file name what we want to render, we can pass data from here also 

def add(request):
    value1 = int(request.POST['num1'])
    value2 = int(request.POST['num2'])
    res = value1+value2 
    return render(request, "result.html",{"result":res})