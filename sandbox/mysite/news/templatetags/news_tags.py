from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    #return Category.objects.all() # Category.objects.filter(news__is_published__contains=1).annotate(cnt=Count('news'))
    return Category.objects.annotate(cnt=Count('news'))


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='hello', arg2='world'):
    #categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    #categories = Category.objects.filter(news__is_published=True).annotate(cnt=Count('news'))
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    # categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    #     cache.set('categories', categories, 30)
    return {"categories":categories, "arg1":arg1, "arg2":arg2}