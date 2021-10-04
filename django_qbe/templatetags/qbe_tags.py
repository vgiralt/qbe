# -*- coding: utf-8 -*-

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def qbe_paginator(total_pages, rows_per_page, current_page):

    def _get_range_markup(range_from, range_to):
        out = []
        for page in range(range_from, range_to):
            if page == current_page:
                html = '<span class="this-page">%s</span>' % (page + 1)
            elif page == 0:
                html = '<a class="start" href="?p=%s">%s</a>' % (page,
                                                                  page + 1)
            elif page == pages - 1:
                html = '<a class="end" href="?p=%s">%s</a>' % (page, page + 1)
            else:
                html = '<a href="?p=%s">%s</a>' % (page, page + 1)
            out.append(html)
        return out

    total_pages = int(total_pages)
    rows_per_page = int(rows_per_page)
    current_page = int(current_page)
    if total_pages < rows_per_page or not rows_per_page:
        pages = 1
    else:
        pages = (total_pages // rows_per_page)
        if total_pages % rows_per_page != 0:
            pages += 1
    output = []
    if pages < 11:
        output += _get_range_markup(0, pages)
    elif current_page < 6:
        output += _get_range_markup(0, current_page + 2)
        output += ["..."]
        output += _get_range_markup(pages - 2, pages)
    elif current_page > pages - 6:
        output += _get_range_markup(0, 2)
        output += ["..."]
        output += _get_range_markup(current_page - 2, pages)
    else:
        output += _get_range_markup(0, 2)
        output += ["..."]
        output += _get_range_markup(current_page - 2, current_page + 3)
        output += ["..."]
        output += _get_range_markup(pages - 2, pages)
    return mark_safe("\n".join(output))
