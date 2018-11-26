from django.urls import path
from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.HomeView.as_view(), name = 'landing'),
    path('posts/', views.PostListView.as_view(), name = 'posts'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name = 'post'),
    # path('home/', views.home_view, name = 'home'),
    # path('index/', views.HomeView.as_view(), name = 'index')
]




