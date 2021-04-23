from django.db import models
from django.urls import reverse   # ---> add
# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=30)
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
    def get_absolute_url(self):       # ---> new function
        url = 'bookview/' + str(self.id)
        return url