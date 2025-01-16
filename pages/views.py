from django.shortcuts import render
# from django.views.generic import ListView,DetailView
#from pages.models import Product
from django.shortcuts import HttpResponse,redirect
# class Home(ListView):
#     model = Product
#     template_name = 'home/index.html'
#     context_object_name = 'productss'


# Create your views here.
def about_page(request):
    return render(request,'about/about-us.html')

def blog_page(request):
    return render( request,'blog/blog.html')

def faq_page(request):
    return render(request,'faq/faq-1.html')

def brands_page(request):
    return render( request,'brands/brands.html')

def home_page(request):

#    pod = Product.objects.all(),{'pod':pod}

    return render(request,'home/index.html')

def contact_page(request):
    return render(request,'contact/contact-1.html')

def login_page(request):
    return render(request,'login_register/login.html')

def register_page(request):
    return render(request,'login_register/register.html')


def brands_page(request):
    return render(request,'brands/brands.html')

def checkout_page(request):
    return render( request,'compare_chekout/checkout.html')

def  compare_page (request):
    return render(request,'compare_chekout/compare.html')

def deliveryreturn_page (request):
    return render( request,'delivery/delivery-return.html')

def shippingdelivery_page(request):
    return render(request,'delivery/shipping-delivery.html')

def paymentconfirmation_page(request):
    return render( request,'payment/payment-confirmation.html')

def paymentfailure_page(request):
    return render(request,'payment/payment-failure.html')

def privacypolicy_page(request):
    return render(request,'privacy_trams/privacy-policy.html')

def termsconditions_page(request):
    return render(request,'privacy_tramsbvcx/terms-conditions.html')

def ordertracking_page(request):
    return render( request,'view_cart/order-tracking.html')

def timeline_page(request):
    return render(request,'view_cart/home-grocery.html')

def viewcart_page(request):
    return render(request,'view_cart/view-cart.html')

def invoice_page(request):
    return render(request,'view_cart/invoice.html')

def wishlist_page(request):
    return render(request,'wishlist/wishlist.html')
