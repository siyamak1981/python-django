from django.urls import reverse_lazy
from django.contrib.sitemaps import Sitemap

class StaticViewsSitemap(Sitemap):
    changefreq='yearly'
    priority = 0.5
    def items(self):
        return ['landing', 'contact']

    def location(self, item):
        return reverse_lazy('mysite:{}'.format(item))