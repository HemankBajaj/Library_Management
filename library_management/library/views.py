from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from django.db import models
from django.contrib.auth.decorators import login_required,user_passes_test
from . import forms,models
from .models import Book
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    form = NewUserForm()
    context = {"form": form}
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    return render(request,"signup.html", context)       

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('userhome')
    else:
        form = AuthenticationForm()
    return render(request, 'userlogin.html', {'form': form})

def userhome(request):
    return render(request, 'userhome.html')

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')

def librlogin(request):
    return render(request, 'librlogin.html')

@login_required(login_url='userlogin')
def bookview(request):
    books=models.Book.objects.all()
    return render(request, 'bookview.html',{'books':books})
@login_required(login_url='userlogin')
def userprofile(request):
    return render(request, 'userprofile.html')

@login_required(login_url='userlogin')
def book_detail(request, pk):
  return render(request, 'book_detail.html', {
    'book': get_object_or_404(Book, id=pk)
  })