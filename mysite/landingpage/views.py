from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request) :
    latest_blogs=BlogPost.objects.order_by('-post_date')[:10]
    context={
        'blog_list':latest_blogs,
             }

    return render(request, 'landingpage/index.html', context)


def about(request) :
    return render(request,'landingpage/about.html',{})


def contact(request) :
    return render(request,'landingpage/contact.html',{})
