from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request) :
    row_wise_blogs=BlogPost.arrange_row_wise(cards_per_row=3)
    featured_blog=BlogPost.objects.get(featured=True)
    context={
        'blog_list':row_wise_blogs,
        'featured_blog':featured_blog,
             }

    return render(request, 'landingpage/index.html', context)


def post(request, post_title):
    post_title=post_title.replace('_',' ')
    blog=BlogPost.objects.get(post_title=post_title)
    context={
        'blog': blog,
    }
    return render( request, 'landingpage/post.html', context )

def about(request) :
    return render(request,'landingpage/about.html',{})


def contact(request) :
    return render(request,'landingpage/contact.html',{})
