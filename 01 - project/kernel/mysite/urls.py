from django.urls import path, re_path
from mysite.sitemap import StaticViewsSitemap
from django.contrib.sitemaps.views import sitemap
from .import views

sitemaps = {
    'static': StaticViewsSitemap,
}

app_name = 'mysite'
urlpatterns = [
    path('', views.HomeView.as_view(), name = 'landing'),
    re_path(r'^contact/$', views.ContactView.as_view(), name = 'contact'),
    re_path(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name = 'sitemap' ),
    path('posts/', views.PostListView.as_view(), name = 'posts'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name = 'post'),
 
    # path('home/', views.home_view, name = 'home'),
    # path('index/', views.HomeView.as_view(), name = 'index')
]




