from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BlogPost
from .forms import NewBlog, EditBlog

# Create your views here.


def blogs(request):

    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


def blog(request, blog_id):

    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)


def new_blog(request):

    if request.method != 'POST':
        form = NewBlog()
    else:
        form = NewBlog(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blog'))
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


def edit_blog(request, edit_id):
    blog = BlogPost.objects.get(id=edit_id)
    if request.method != 'POST':
        form = EditBlog(instance=blog)
    else:
        form = EditBlog(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

























