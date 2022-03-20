from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms

# Create your views here.
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

def log(request):
    if not request.user.is_authenticated:
        return render(request,"login1.html",{"message":None})
    
    context={
        "user":request.user
    }
    return render(request,"home.html",context)

def login_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("log"))
    else:
        return render(request,"login1.html",{"message":"invalid credential." })      




def logout_view(request):
    logout(request)
    return render(request,"login1.html",{"message":"Logged out"})


def registerPage(request):
    form=CreateUserForms()
    
    if request.method == 'POST':
        form = CreateUserForms(request.POST)
        if form.is_valid():
            form.save()
    
    context={"form":form}
    return render(request,"register.html",context)



   

def signup_view(request):
    return render(request,"register.html")