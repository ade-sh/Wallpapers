from django import template

register = template.Library()


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


@register.filter
def addstrpage(arg1):
    """concatenate arg1 & arg2"""
    return str(arg1-1) + str(arg1)+ str(arg1+1)
