from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
    path("", views.index,name="index"),
    path("<slug:slug>",views.details,name="blogDetail"),
    path("allposts/",views.allPosts,name="allPosts"),
    ]