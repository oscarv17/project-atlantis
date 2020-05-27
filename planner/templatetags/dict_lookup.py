from django.template.defaulttags import register
from planner.models import MONTHS

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, 0.0)

@register.filter
def diff(act, curr):
    return (curr - act)

@register.filter
def months(month_number):
    return MONTHS.get(month_number)