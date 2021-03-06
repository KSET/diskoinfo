from django import template
import re

register = template.Library()


@register.simple_tag
def search(string, pattern, result_true, result_false):
    if string and pattern and re.search(pattern, string):
        return result_true
    return result_false


# use for class=active in navbar
@register.simple_tag
def active(request, pattern):
    return search(request.path, pattern, result_true='active', result_false='') if request else ''


@register.simple_tag
def flash_msg_tags(msg):
    if not msg.tags:
        return ''
    if msg.tags == 'error':
        return 'alert-%s' % 'danger'
    return 'alert-%s' % msg.tags


@register.simple_tag
def user_info(user):
    name = '%s %s' % (user.first_name, user.last_name)
    if not name.strip():
        name = user.username
    return name
