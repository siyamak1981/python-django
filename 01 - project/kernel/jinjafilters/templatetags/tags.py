from django import template
from khayyam import JalaliDate
from khayyam import JalaliDatetime

from blog.models import Comment

register = template.Library()

@register.filter(name = 'jalali_date')
def persian_date(date):
    return JalaliDate(date).strftime('%K-%R-%n')

@register.filter(name = 'jalali_time')
def persian_time(date):
    return JalaliDatetime(date).strftime('%K:%r')

@register.filter(name = 'len_comment')
def get_comment_length(post):
    cm = Comment.objects.filter(for_post = post)
    return len(cm)