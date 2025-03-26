from django import template

register = template.Library()

@register.simple_tag
def upper_words(value):
   return value.upper()