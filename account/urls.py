"""
URL configuration for emart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from account.views import  ResetPassword,PasswordResetSent,ForgotPassword,address_page ,editaccount_page ,login_page ,logout_page,singup_page ,ordersdetails_page , orders_page,wishlist_page,myaccount_page
from . import views
urlpatterns = [

# home_page URLs start
    path('address/' , address_page , name="address"),
    path('editaccount/' , editaccount_page , name="editaccount"),
    path('ordersdetails/' , ordersdetails_page , name="ordersdetails"),
    path('orders/' , orders_page , name="orders"),
    path('wishlist/' , wishlist_page , name="wishlist"),
    path('myaccount/' , myaccount_page , name="myaccount"),
    path('login/' , login_page , name="login"),
    path('logout/' , logout_page , name="logout"),
    path('register/' , singup_page , name="register"),

    path('forgot-password/', ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/',PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', ResetPassword, name='reset-password'),




]
