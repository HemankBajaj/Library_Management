from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book,Review, IssueRequest


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude=['user','book']

class IssueRequestForm(forms.ModelForm):
    class Meta:
        model = IssueRequest
        exclude = ['user','book', 'permission', 'status','returned','issue_date','return_date']
