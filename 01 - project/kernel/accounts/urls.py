from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'
urlpatterns = [
    re_path(r'^signup/$', views.SignUp.as_view(), name = 'signup'),
    re_path(r'^signin/$', views.SignIn.as_view(), name = 'signin'),
    re_path(r'^signout/$', views.SignOut.as_view(), name = 'signout'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.Activate.as_view(), name = 'activation'),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]