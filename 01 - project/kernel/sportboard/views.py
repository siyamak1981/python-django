from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
from .models import Category
from .models import Roles
from .models import City
from .models import Tag
from .models import Bosses
# Create your views here.

class BossListView(ListView):
    model = Bosses
    template_name = 'sportboard/boss_list.html'
    context_object_name = 'bosses'
    paginate_by = 2
    page_name = ' رئسا '
    

class BossDetailView(DetailView):
    model = Bosses
    template_name = 'sportboard/boss_detail.html'
    context_object_name = 'boss'
    page_name = ' ریس '
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(BossDetailView, self).get_context_data(*args, **kwargs)
        context['latest_post'] = Post.objects.all()
        return context
   

class BossTempalteView(TemplateView):
    model = Bosses
    template_name = 'sportboard/boss_bio.html'
    context_object_name = 'bio'
    page_name = ' بیوگرافی '


class BossTableView(TemplateView):
    model = Bosses
    template_name = 'sportboard/boss_table.html'
    context_object_name = 'boss_table'
    page_name = ' لیست روسا '

class BossTreeView(TemplateView):
    
    template_name = 'sportboard/boss_tree.html'
    context_object_name = 'boss_tree'
    page_name = ' لیست روسا '

class BossLeagueView(TemplateView):

    template_name = 'sportboard/league.html'
    context_object_name = ' league '
    page_name = 'لیست روسا '