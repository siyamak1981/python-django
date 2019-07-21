from django.urls import path, re_path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'
urlpatterns = [
    # path('posts/', views.PostListView.as_view(), name = 'posts'),
    path('posts/', views.post_list, name = 'posts'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    # path('post/<slug:slug>', views.PostDetailView.as_view(), name = 'post'),
    path('feed/', LatestPostFeed(), name = 'feeds'),
    
]