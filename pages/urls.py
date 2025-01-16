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
from pages import views
from django.urls import path,include
from pages.views import home_page,blog_page,faq_page,brands_page,compare_page,contact_page,about_page,brands_page ,invoice_page ,wishlist_page ,viewcart_page , timeline_page , ordertracking_page ,checkout_page ,termsconditions_page ,privacypolicy_page ,paymentfailure_page ,paymentconfirmation_page , deliveryreturn_page ,shippingdelivery_page
urlpatterns = [

# home_page URLs start

path('' , views.home_page , name="home"),
path('about/' , about_page , name="about"),
path('blog/' ,  blog_page , name="blog"),
path('faq/' ,  faq_page , name="faq"),
path('brands/' ,  brands_page , name="brands"),
path('contact/' , contact_page , name="contact"),
path('brands/' , brands_page , name="brands"),
path('checkout/' , checkout_page , name="checkout"),
path('compare/' , compare_page , name="compare"),
path('deliveryreturn/' , deliveryreturn_page , name="deliveryreturn"),
path('shippingdelivery/' , shippingdelivery_page , name="shippingdelivery"),
path('paymentconfirmation/' , paymentconfirmation_page , name="paymentconfirmation"),
path('paymentfailure/' , paymentfailure_page , name="paymentfailure"),
path('privacypolicy/' , privacypolicy_page , name="privacypolicy"),
path('termsconditions/' ,termsconditions_page , name="termsconditions"),
path('invoice/' ,  invoice_page , name="invoice"),
path('ordertracking/' , ordertracking_page , name="ordertracking"),
path('timeline/' , timeline_page , name="timeline"),
path('viewcart/' , viewcart_page , name="viewcart"),
path('wishlist/' , wishlist_page , name="style"),





]
