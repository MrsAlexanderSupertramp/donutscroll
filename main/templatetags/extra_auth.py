from django import template
from django.contrib.auth.models import Group
from news.models import News

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='bottom_news')
def bottom_news(number):
    return News.objects.all().order_by('-pk')[: number]
