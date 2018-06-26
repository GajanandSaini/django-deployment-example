from django import template

register= template.Library()


def cut(arg1,arg2):
    return arg1.replace(arg2,'')



register.filter('cut',cut)
