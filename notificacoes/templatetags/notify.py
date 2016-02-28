# coding: utf-8

from django import template


register = template.Library()


@register.inclusion_tag('notification/notification.html')
def render_notification():
    return {}


@register.filter
def format_hello(value, nome):
    return value % (nome)
