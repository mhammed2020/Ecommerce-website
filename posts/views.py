from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage

# Create your views here.

def index(request) :
    posts = Product.objects.all()
    paginator = Paginator(posts,8)  # Show 25 contacts per page.
    page= request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_page)


    context={'posts':posts,
              'page' : page,
             }
    return render(request,'index.html',context)
def details(request,id) :
    posts = Product.objects.get(id = id)
    context={'posts':posts}

    return render(request,'details.html',context)

