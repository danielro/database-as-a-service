# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag(takes_context=False)
def status_color(status_code):
    status_map = {
        0: 'info',
        1: 'warning',
        2: 'success',
        3: 'error'
    }
    return status_map.get(status_code)


@register.simple_tag(takes_context=False)
def get_notes_for(task):
    if task.method_path == 'update_ssl':
        return ('SSL Certificate will expire at {}. Please update before '
                'this date.').format(
            task.database.infra.earliest_ssl_expire_at.strftime('%Y-%m-%d')
        )

    return '-'
