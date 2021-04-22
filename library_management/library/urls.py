from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('librlogin', views.librlogin, name='librlogin'),
    path('userhome', views.userhome, name='userhome'),
    path('logout', views.logoutuser, name='logout')
]