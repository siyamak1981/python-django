from django.urls import path, re_path
from mysite.sitemap import StaticViewsSitemap
from django.contrib.sitemaps.views import sitemap
from .import views

sitemaps = {
    'static': StaticViewsSitemap,
}

app_name = 'mysite'
urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name = 'landing'),
    re_path(r'^contact/$', views.ContactView.as_view(), name = 'contact'),
    re_path(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name = 'sitemap' ),
  
 
]




