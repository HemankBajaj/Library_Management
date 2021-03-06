from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('librlogin', views.librlogin, name='librlogin'),
    path('userhome', views.userhome, name='userhome'),
    path('logout', views.logoutuser, name='logout'),
    path('bookview', views.bookview, name='bookview'),
    path('userprofile', views.userprofile, name = 'userprofile'),
    path('bookview/<int:pk>', views.book_detail, name='book_detail'),
    path('bookview/addbook',views.addbook, name="addbook"),
    path('addbook',views.addbook, name="addbook"),
    path('bookview/bookview', views.bookview, name='bookview'),
    path('bookview/bookview/<int:pk>', views.book_detail, name='book_detail'),
    path('bookview/review/<int:pk>', views.review_delete, name='review_delete'),
    path('search/', views.SearchPage, name='search_result'),
    path('bookview/delete_book/<int:pk>', views.delete_book, name='bookdelete'),
    path('pending', views.pending, name ='pending'),
    path('issue/<int:pk>',views.issue, name='issue'),
    path('issued', views.issued, name='issued'),
    path('return_book/<int:pk>', views.return_book, name = 'return')
]