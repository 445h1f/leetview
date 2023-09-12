from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# filter to get value of key in dict
@register.filter(name="getValue")
def getValue(dictionary, key):
    return dictionary.get(key)

@register.filter
@stringfilter
def title(value):
    return value.title()