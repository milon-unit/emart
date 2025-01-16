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
from shop.views import collectionlist_page,default_page,women_page,rightsidebar_page,men_page,loadmore_page,leftsidebar_page,shoplink_page,scrolling_page,filterhidden_page,filtersidebar_page

urlpatterns = [

# home_page URLs start
    path('collectionlist/' , collectionlist_page , name="collectionlist"),
    path('default/' , default_page , name="default"),
    path('filterhidden/' , filterhidden_page , name="filterhidden"),
    path('filtersidebar/' , filtersidebar_page , name="filtersidebar"),
    path('scrolling/' , scrolling_page , name="scrolling"),
    path('rightsidebar/' , rightsidebar_page , name="rightsidebar"),
    path('leftsidebar/' , leftsidebar_page , name="leftsidebar"),
    path('shoplink/' ,shoplink_page , name="shoplink"),
    path('loadmore/' ,  loadmore_page , name="loadmore"),
    path('men/' , men_page , name="men"),
    path('women/' , women_page , name="women"),





]
