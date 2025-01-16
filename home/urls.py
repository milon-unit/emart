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
from home.views import tee_page,skincare_page,skateboard_page,search_page,pod_store_page,phonecase_page,electronic_page,dog_accessories_page,accessories_page,decor_page,baby_page,activewear_page,furniture_page,giftcard_page,glasses_page,grocery_page,handbag_page,headphone_page,jewerly_page,kids_page,kitchen_wear_page,men_page,multi_brand_page,paddle_boards_page,sneaker_page,sock_page,stroller_page

urlpatterns = [


# home_page URLs start
    path('accessories/' , accessories_page , name="accessories"),
    path('decor/' , decor_page , name="decor"),
    path('baby/' , baby_page , name="baby"),
    path('activewear/' , activewear_page , name="activewear"),
    path('dogaccessories/' , dog_accessories_page , name="dogaccessories"),
    path('electronic/' , electronic_page , name="electronic"),
    path('furniture/' , furniture_page , name="furniture"),
    path('giftcard/' , giftcard_page , name="giftcard"),
    path('glasses/' , glasses_page , name="glasses"),
    path('grocery/' , grocery_page , name="grocery"),
    path('handbag/' , handbag_page , name="handbag"),
    path('headphone/' , headphone_page , name="headphone"),
    path('jewerly/' , jewerly_page , name="jewerly"),
    path('kids/' , kids_page , name="kids"),
    path('kitchenwear/' , kitchen_wear_page , name="kitchenwear"),
    path('men/' , men_page , name="men"),
    path('multibrand/' , multi_brand_page , name="multibrand"),
    path('paddleboards/' , paddle_boards_page , name="paddleboards"),
    path('phonecase/' , phonecase_page , name="phonecase"),
    path('podstore/' , pod_store_page , name="podstore"),
    path('search/' , search_page , name="search"),
    path('skateboard/' , skateboard_page , name="setupgear"),
    path('skincare/' , skincare_page , name="skincare"),
    path('sneaker/' , sneaker_page , name="sneaker"),
    path('sock/' , sock_page , name="sock"),
    path('stroller/' , stroller_page , name="stroller"),
    path('tee/' , tee_page , name="tee"),




]
