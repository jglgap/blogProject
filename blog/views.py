from django.shortcuts import render
from .models import Post, Author, Tag
from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html",{"posts":posts})

# def details(request,slug):
#     try:
#         post = Post.objects.get(slug=slug)
#     except:
#         raise Http404()
#     return render(request,"blog/detail.html",{
#         "title": post.title,
#         "exceptText":post.exceptText,
#         "imageName":post.image.url,
#         "date":post.date,
#         "content":post.content,
#         'author':post.author,
#         'tags': post.tag.all(),
#     })

# def allPosts(request):
#     allPost = Post.objects.all().order_by("-date")
#     return render(request,"blog/allPosts.html",{"posts":allPost})

class Index(ListView):
   template_name="blog/index.html"
   model = Post
   context_object_name="posts"
#    ordering= ["-date"]
   def get_queryset(self):
      return Post.objects.all().order_by('-date')[:3]
    #   queryset = super().get_queryset()
    #   data = queryset[:3]
    #   return data
class AllPost(ListView):
    template_name = "blog/allPosts.html"
    model = Post
    context_object_name = "posts"

# class Details(DetailView):
#    template_name = "blog/detail.html"
#    model = Post


class Details(View):

   def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post" : post,
            "post_tags" : post.tag.all(),
            # "comment_form" : CommentForm()
    #    comments = post.comments.all()
        }
        return render(request,"blog/detail.html",context)
   
   def post(self,request,slug):
    #    comment_form : CommentForm(request.Post)
        #post : Post.objects.get(slug=slug)
    # if comment_form.is_valid():
    #    comment = comment_form.save(commit=False)
    #    comment.post = post
    #    comment.save()
    #    return HttpResponseRedirect(reverse("blogDetail",args=[slug]))
      post = Post.objects.get(slug=slug)
      context = {
            "post" : post,
            "post_tags" : post.tag.all(),
            # "comment_form" : CommentForm()
        #    comments = post.comments.all()

        }
      return render(request,"blog/detail.html",context)