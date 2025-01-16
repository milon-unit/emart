from django.shortcuts import render

# Create your views here.
def blogdetail_page(request):
    return render(request,'blog/blog-detail.html')

def bloggrid_page(request):
    return render( request,'blog/blog-grid.html')

def  bloglist_page(request):
    return render(request,'blog/blog-list.html')

def sidebarleft_page(request):
    return render( request,'blog/blog-sidebar-left.html')

def  sidebarright_page(request):
    return render(request,'blog/blog-sidebar-right.html')
