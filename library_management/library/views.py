from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm, BookForm, ReviewForm
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
    reviews=models.Review.objects.filter(user=request.user)
    return render(request, 'userprofile.html',locals())

@login_required(login_url='userlogin')
def book_detail(request, pk):
    book =  get_object_or_404(Book, id=pk)
    reviews=models.Review.objects.filter(book=book)
    n = len(reviews)
    final_rate= 0
    for review in reviews:
        final_rate+=int(review.rating)
    if n>0:
        final_rate /= n
    review_form = ReviewForm()
    if request.method =="POST":
         review_form = ReviewForm(request.POST)
         if review_form.is_valid():
            rev = review_form.save(commit=False)
            rev.user = request.user
            rev.book = book
            rev.save()
            return HttpResponse('Review Submitted')
    return render(request, 'book_detail.html', locals())





def addbook(request):
    book_form = BookForm()
    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('bookview')
    return render(request,'addbook.html', {'book_form':book_form})

