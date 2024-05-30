from django import template

register = template.Library()

@register.filter
def in_category(value, category_list):
    return value in category_list.split(',')
