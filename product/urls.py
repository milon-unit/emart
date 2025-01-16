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
from product.views import accordion_page,boughttogether_page,customizer_page,notification_page,stacked_page,style_page,stylelist_page,productvideo_page ,quickorder_page,preorders_page,pickup_page,descriptionlist_page,productdetail_page,giftcard_page,grid_page

urlpatterns = [

# home_page URLs start
    # path('accordion/' , accordion_page , name="accordion"),
    # path('accordion/' , accordion_page , name="accordion"),
    path('descriptionlist/' , descriptionlist_page , name="descriptionlist"),
    path('productdetail/' , productdetail_page , name="productdetail"),
    

















    path('accordion/',accordion_page,name='accordion'),
    path('boughttogether/' , boughttogether_page , name="boughttogether"),
    path('customizer/' , customizer_page , name="customizer"),
    path('giftcard/' , giftcard_page , name="giftcard"),
    path('grid/' , grid_page , name="grid"),
    path('giftcard/' , giftcard_page , name="giftcard"),
    path('notification/' ,notification_page , name="notification"),
    path('pickup/' ,  pickup_page , name="pickup"),
    path('preorders/' , preorders_page , name="preorders"),
    path('quickorder/' , quickorder_page , name="quickorder"),
    path('stacked/' , stacked_page , name="stacked"),
    path('style/' , style_page , name="style"),
    path('stylelist/' , stylelist_page , name="stylelist"),
    path('productvideo/' , productvideo_page , name="productvideo"),




]
