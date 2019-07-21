from django import template
from ..models import Post


register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.all().count()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.all().order_by('-published_at')[:count]
    return {'latest_posts': latest_posts}