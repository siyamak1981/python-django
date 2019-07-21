from django.urls import  re_path
from . import views


app_name = 'sportboard'
urlpatterns = [
    re_path(r'^posts/$', views.BossListView.as_view(), name = 'news'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.BossDetailView.as_view(), name = 'new'),
    re_path(r'^bio/(?P<firstname>[-\w]+)/$', views.BossTempalteView.as_view(), name = 'bio'),
    re_path(r'^boss/boss_table/$', views.BossTableView.as_view(), name = 'boss_table'),
    re_path(r'^boss/boss_tree/$', views.BossTreeView.as_view(), name = 'boss_tree'),
    re_path(r'^boss/league/$', views.BossLeagueView.as_view(), name = 'league'),
    
]