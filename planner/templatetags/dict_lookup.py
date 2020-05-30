from django.template.defaulttags import register

from planner.models import MONTHS

@register.filter
def get_item(dictionary, key):
    ''' Returns a item from a dictionary '''
    return dictionary.get(key, 0.0)

@register.filter
def diff(act, curr):
    ''' Returns the difference between two amounts '''
    return curr - act

@register.filter
def months(month_number):
    ''' Returns the month name from a month number '''
    return MONTHS.get(month_number)
    