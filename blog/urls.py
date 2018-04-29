from django.contrib import admin
from django.conf.urls import url
from blog.views import *

app_name = 'blog'


urlpatterns = [
    url(r"^$", index, name="home" ),
    url(r"^blog/$", blog_list, name="blog"),
    url(r"^blog/(?P<id>[0-9]+)/$", blog_detail, name="details"),
    url(r"^blog/create/$", add_blog, name="create"),
    url(r"^blog/(?P<id>[0-9]+)/edit/$", edit_blog, name="update"),
    url(r"^blog/(?P<id>[0-9]+)/delete/$", delete_blog, name="delete"),
    
]