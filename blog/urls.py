from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
    path("", views.Index.as_view(),name="index"),
    path("<slug:slug>",views.Details.as_view(),name="blogDetail"),
    path("allposts/",views.AllPost.as_view(),name="allPosts"),
    ]