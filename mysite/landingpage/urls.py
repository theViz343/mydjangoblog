from django.urls import include, path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('posts/<post_title>',views.post,name='post'),
    path('section/<section_tag>',views.section,name='section'),
    path('donate',views.donate,name='donate'),
    path('search',views.search,name='search'),
]