from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# 自定义过滤器
@register.filter
def my_filter(v1, v2):
    return v1 * v2


# 自定义标签
@register.simple_tag
def my_tag1(v1, v2, v3):
    return v1 * v2 * v3


# 语义化标签
@register.simple_tag
def my_html_tag(v1, v2):
    temp_html = "<input type='text' id = '%s' class='%s'>" % (v1, v2)
    return mark_safe(temp_html)
