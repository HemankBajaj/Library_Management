from django.db import models
from django.urls import reverse   # ---> add
from django.contrib.auth.models import User


# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=50)
    genre_choice= [
        ('academics', 'Academics'),
        ('fiction', 'Fiction'),
        ('action ', 'Action '),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('mystery','Mystery'),
        ('fantasy','Fantasy')
        ]
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    genre=models.CharField(max_length=30,choices=genre_choice,default='academics')
    number = models.PositiveIntegerField()
    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        return reverse('bookview', args=[str(self.id)])




class Review(models.Model):
    review=models.CharField(max_length=200,default="none")
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'), 
    )
    rating=models.CharField(max_length=2,choices=CHOICES,default='5')

    def __str__(self):
        s1 = self.book.title
        s2 = self.user.username
        s4 = self.review

        return "["+ s1 + "] [" + s2 + "] " + " " + s4

class IssueRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    permissions = ((False,'denied'),(True,'issued'))
    statu = ((False,'pending'),(True,'seen'))
    status=models.BooleanField(max_length=30,choices=statu,default=False)
    permission=models.BooleanField(max_length=30,choices=permissions,default=False)
    def __str__(self):
        if not self.permission and not self.status:
            return "Pending "+ self.user.username + " " + self.book.title
        if not self.permission and self.status:
            return "Rejected " + self.user.username + " " + self.book.title
        if self.permissions and self.status:
            return "Accepted " + self.user.username + " " + self.book.title

