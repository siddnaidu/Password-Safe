from typing import KeysView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/<int:account_id>', views.account, name='account'),
    path('account_creation', views.account_creation, name='account_creation'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logOutUser, name='logout')
]