import datetime
from django import template



register = template.Library()


# cutom filter:


def cutter(value, arg):
    return value[:arg]



register.filter(cutter)


# custom tag:




@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string) 