from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms
from .models import BlogPost
from datetime import datetime

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


def about(request):
    return render(request,"about.html")


def blogs(request):
    '''get all the data from the database and display it in the blogs.html'''
    posts = BlogPost.objects.all().order_by('-date_posted')
    print(posts)
    context = {'posts': posts}   

    return render(request,"article.html",context)

def add(request):
    return render(request,"add.html")


def post(request):
    '''get inputs from the from add.html and post the inputs to the database Blogpost and after that redirect to url blogs'''
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        subtitle = request.POST['subtitle']
        BlogPost.objects.create(title=title, content=content, author=author, subtitle=subtitle, date_posted=datetime.now())
        return HttpResponseRedirect(reverse('blogs'))
    else:
        return render(request, 'add.html')


def detail(request, id):
    '''get the id of the post and display the post in detail.html'''
    post = BlogPost.objects.get(id=id)
    context = {'post': post}
    return render(request, 'detail.html', context)
    