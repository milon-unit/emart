from django.shortcuts import render

# Create your views here.
def collectionlist_page(request):
    return render(request,'shop/shop-collection-list.html')

def default_page(request):
    return render( request,'shop/shop-default.html')

def filterhidden_page(request):
    return render(request,'shop/shop-filter-hidden.html')

def filtersidebar_page(request):
    return render( request,'shop/shop-filter-sidebar.html')

def scrolling_page(request):
    return render(request,'shop/shop-infinite-scrolling.html')

def leftsidebar_page(request):
    return render(request,'shop/product-giftcard.html')

def shoplink_page(request):
    return render(request,'shop/shop-link.html')

def loadmore_page(request):
    return render(request,'shop/product-notification.html')

def men_page(request):
    return render( request,'shop/shop-men.html')

def rightsidebar_page(request):
    return render(request,'shop/shop-right-sidebar.html')

def women_page(request):
    return render(request,'shop/shop-women.html')
