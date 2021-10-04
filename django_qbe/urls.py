# -*- coding: utf-8 -*-
from django.urls import path, re_path
from django_qbe.exports import formats

from .views import qbe_form
from .views import qbe_js
from .views import qbe_bookmark
from .views import qbe_proxy
from .views import qbe_autocomplete
from .views import qbe_export
from .views import qbe_results

urlpatterns = [
    path('qbe.js', qbe_js, name="qbe_js"),
    path('bookmark/', qbe_bookmark, name="qbe_bookmark"),
    path('proxy/', qbe_proxy, name="qbe_proxy"),
    path('auto/', qbe_autocomplete, name="qbe_autocomplete"),
    re_path('(?P<query_hash>(.*))/results\.(?P<format>(%s))$' % "|".join(list(formats.keys())), qbe_export, name="qbe_export"),
    path('<str:query_hash>/results/', qbe_results, name="qbe_results"),
    path('<str:query_hash>/', qbe_form, name="qbe_form"),
    path('', qbe_form, name="qbe_form"),
]
