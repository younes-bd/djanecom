from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Product


class LatestProductFeed(Feed):
    title = 'My shop'
    link = reverse_lazy('shop:products')
    description = 'New product of my shop.'

    def items(self):
        return Product.objects.all()[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return truncatewords(item.description, 30)
