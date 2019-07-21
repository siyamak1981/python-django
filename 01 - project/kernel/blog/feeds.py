from django.urls import reverse
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from blog.models import Post


class LatestPostFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.posts.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_link(self, item):
        return reverse("blog:post", args = [item.pk])

