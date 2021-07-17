import dataclasses

from django import template

register = template.Library()


@register.filter
def replacespace(value):
    return str(value).replace("#", " sharp").replace(" ", "_").lower()


@register.filter
def range_filter(value):
    return value[0:150] + '.....'

# register.filter('replace', replace)
