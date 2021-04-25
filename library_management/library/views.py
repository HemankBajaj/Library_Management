from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm, BookForm, ReviewForm, IssueRequestForm
from django.db import models
from django.contrib.auth.decorators import login_required,user_passes_test
from . import forms,models
from .models import Book,Review, IssueRequest
import datetime as DT

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
    requests = models.IssueRequest.objects.filter(user = request.user)
    return render(request, 'userprofile.html',locals())

@login_required(login_url='userlogin')
def book_detail(request, pk):
    book =  get_object_or_404(Book, id=pk)
    reviews=models.Review.objects.filter(book=book)
    n = len(reviews)
    user = request.user
    final_rate= 0
    irequest = IssueRequestForm()
    form = BookForm(instance = book)
    requ = models.IssueRequest.objects.filter(book=book, user= user)
    for review in reviews:
        final_rate+=int(review.rating)
    if n>0:
        final_rate /= n
    review_form = ReviewForm()
    if request.method =="POST":
        if "add_review" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                rev = review_form.save(commit=False)
                rev.user = request.user
                rev.book = book
                rev.save()
                return HttpResponse('Review Submitted')
        elif "ISSUE BOOK" in request.POST:
            irequest = IssueRequestForm(request.POST)
            if irequest.is_valid():
                req = irequest.save(commit=False)
                req.book = book
                req.user = request.user
                req.save()
                return redirect('userprofile')
        else:
            form = BookForm(request.POST,instance=book)
            if form.is_valid():
                book1 = form.save(commit=False)
                book1.save()
                return HttpResponse('Book Successfully Updated')
    
    return render(request, 'book_detail.html', locals())

def SearchPage(request):
    srh = request.GET['query']
    books = models.Book.objects.filter(title__icontains=srh)
    books = {'books': books, 'search':srh}
    return render(request, 'bookview.html', books)



def addbook(request):
    book_form = BookForm()
    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('userhome')
    return render(request,'addbook.html', {'book_form':book_form})


@login_required(login_url='userlogin')
def review_delete(request,pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        review.delete()
        return HttpResponse('Comment Successfully Deleted')



@login_required(login_url='userlogin')
def delete_book(request,pk):
    book = get_object_or_404(Book, id=pk)
    reviews=models.Review.objects.filter(book=book)
    if request.method == "POST":
        book.delete()
        for review in reviews:
            review.delete()
        return redirect('userhome')

def pending(request):
    requests = models.IssueRequest.objects.all()
    today = DT.date.today()
    return render(request, 'pending.html',locals())

@login_required(login_url='userlogin')
def issue(request, pk):
    user = request.user()
    req = get_object_or_404(IssueRequest,id =pk)
    req_form = IssueRequestForm(instance = req)
    book = req.book
    today = DT.date.today()
    week_after = today + DT.timedelta(days=7)
    if request.method =="POST":
        if "issue" in request.POST:
            req_form = IssueRequestForm(request.POST, instance = req)
            if req_form.is_valid():
                r = req_form.save(commit=False)
                r.permission =True
                r.status = True
                r.return_date = week_after
                r.issue_date = today
                book.number -= 1
                book.save()
                r.save()
                return HttpResponse("BOOK ISSUED")
        else:
            req_form = IssueRequestForm(request.POST, instance = req)
            if req_form.is_valid():
                r = req_form.save(commit=False)
                r.permission =False
                r.status = True
                r.save()
                return HttpResponse("Issue Declined Successfully")

def issued(request):
    requests = models.IssueRequest.objects.filter(returned=False, permission = True)
    return render(request, 'issued.html', locals())


    