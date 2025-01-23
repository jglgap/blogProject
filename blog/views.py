from django.shortcuts import render
from .models import Post, Author, Tag
from django.http import Http404
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{"posts":posts})

def details(request,slug):
    try:
        post = Post.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request,"blog/detail.html",{
        "title": post.title,
        "exceptText":post.exceptText,
        "imageName":post.image_name,
        "date":post.date,
        "content":post.content,
        'author':post.author,
        'tags': post.tag.all(),
    })

def allPosts(request):
    allPost = Post.objects.all().order_by("-date")
    return render(request,"blog/allPosts.html",{"posts":allPost})