from django.urls import path
from django.conf.urls import url
from . import views

from django.urls import path
app_name = 'shop'

urlpatterns = [
    # url(r'^$', views.ShopListView.as_view(), name = 'products'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.ShopListView.as_view(), name = 'product_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.ShopDetailView.as_view(), name = 'product'),
    # path('/<slug:slug>', views.CategoryDetail.as_view(), name = 'category'),
    path('list/', views.product_list, name='products'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name ='product_detail'),
    # url(r'^cart/$', views.CardTemplateView.as_view(), name = 'cart_add'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

