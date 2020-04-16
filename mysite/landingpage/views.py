from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost, CustomTag

# Create your views here.
def index(request) :
    row_wise_blogs=BlogPost.objects.order_by( '-post_date' )[:10]
    featured_blog=BlogPost.objects.get(featured=True)
    context={
        'blog_list':row_wise_blogs,
        'featured_blog':featured_blog,
             }

    return render(request, 'landingpage/newindex.html', context)


def post(request, post_title):
    post_title=post_title.replace('_',' ')
    blog=BlogPost.objects.get(post_title=post_title)
    context={
        'blog': blog,
    }
    return render( request, 'landingpage/newpost.html', context )

def donate(request) :
    return render(request,'landingpage/donate.html',{})

def contact(request) :
    return render(request,'landingpage/contact.html',{})

def section(request,section_tag):
    section_blogs=BlogPost.get_posts_with_tag(section_tag)
    section_color="gray"
    if section_tag.lower()=="politics":
        section_color="orange"
    elif section_tag.lower()=="entertainment":
        section_color="tomato"
    elif section_tag.lower()=="technology":
        section_color="dodgerblue"
    elif section_tag.lower()=="business":
        section_color="mediumseagreen"
    context={
        'blog_list': section_blogs,
        'title': section_tag,
        'section_color': section_color,
    }
    return render( request, 'landingpage/newsection.html', context )

def search(request):

    if request.GET:
        search_string=str(request.GET['search'])

    search_query=search_string.split(' ')
    results=[]
    for query in search_query:
        try:
            query_matches = CustomTag.objects.filter(tag__iexact=query)
            for match in query_matches:
                results.extend( match.get_blogs() )
        except:
            continue

    row_wise_blogs = []
    for i in range( 0, len( results ), 3 ) :
        if len( results ) - i >= 3 :
            row_wise_blogs.append( results[i :i + 3] )
        else :
            row_wise_blogs.append( results[i : len( results )] )

    context={
        'search_string': search_string,
        'results': row_wise_blogs,
    }
    return render(request,'landingpage/search.html',context)