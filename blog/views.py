from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from django.urls import reverse
from blog.models import Blog
from django.contrib.auth.models import User

from blog.forms import BlogForm

def index(request):
    title = "Welcome To Edge"
    context = {
        'title': title
    }
    return render(request, "blog/index.html", context)

def blog_list(request):
    all_blog = Blog.objects.all().order_by("-created_at")
    paginator = Paginator(all_blog, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    title = "All my blog post"
    context = {
        'title': title,
        'blogs': blogs
    }
    return render(request, "blog/blog_list.html", context)

"""

def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'list.html', {'contacts': contacts})
"""


def blog_detail(request, id=None):
    blog = get_object_or_404(Blog, id=id)
    context = {
        'blog': blog
    }
    return render(request, "blog/blog_detail.html", context)

def add_blog(request):
    if not request.user.is_staff or not request.user.is_superuser:
    	raise Http404
    title = "Create"
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog            = form.save(commit=False)
            blog.author     = request.user
            blog.created_at = timezone.now()
            blog.save()
            return redirect("details", blog.id)
    else:
        form = BlogForm()
        return render(request, "blog/form.html", {"form": form, "title": title})

def edit_blog(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    blog = get_object_or_404(Blog, id=id)
    title = "Update"
    #form = BlogForm(request.POST or None, instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        #form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.created_at = timezone.now()
            blog.save()
            return redirect("blog:blog")
    else:
        form = BlogForm(instance=blog)
        return render(request, "blog/form.html", {"form": form, "title": title})

def delete_blog(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if request.user.is_superuser:
        blog = get_object_or_404(Blog, id=id)
        title = "Delete Page"
    else:
        blog = get_object_or_404(Blog, id=id, author=request.user)
    if request.method == "POST":
        blog.delete()
        return redirect(reverse("blog:blog"))
    else:
        return render(request, "blog/delete.html", {"blog": blog,"title": title})
