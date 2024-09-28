from django.urls import path
from . import views



urlpatterns = [
    path('', views.posts_list, name="posts_list"),
    path('<slug:slug>', views.post_page, name="post_page"),
    path('new-post/', views.new_post, name="new-post")
]