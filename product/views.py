from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Product
from product import views
app_name = 'product'
# Create your views here.
#def wishlist(request):
def product_list(request,category_slug):
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter.all()
    if category_slug:
        category = get_absolute_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,'product/product_list.html',{
          'category':category,
          'products':products,
          'categories':categories,
    })


def product_detail(request,id,slug):
    products = get_absolute_or_404(Product,id=id,slug=slug,available=True)
    return render(request,'product/product_detail.html',{'product':product}) 




















def accordion_page(request):
    return render(request,'product/product-accordion.html')

def boughttogether_page(request):
    return render( request,'product/product-bought-together.html')

def customizer_page(request):
    return render(request,'product/product-customizer.html')

def descriptionlist_page(request):
    return render( request,'product/product-description-list.html')

def productdetail_page(request):
    return render(request,'product/product-detail.html')

def giftcard_page(request):
    return render(request,'product/product-giftcard.html')

def grid_page(request):
    return render(request,'product/product-grid.html')

def notification_page(request):
    return render(request,'product/product-notification.html')

def pickup_page(request):
    return render( request,'brands/product-pickup.html')

def preorders_page(request):
    return render(request,'product/product-pre-orders.html')

def quickorder_page(request):
    return render(request,'product/product-quick-order.html')

def stacked_page(request):
    return render(request,'product/product-stacked.html')

def style_page(request):
    return render(request,'product/product-style-01.html')

def stylelist_page(request):
    return render(request,'product/product-style-list.html')

def productvideo_page(request):
    return render(request,'product/product-video.html')
