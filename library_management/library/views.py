from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login
from django.contrib import messages #import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
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