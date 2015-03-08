"""Django Desktop Application View Module

This module contains the views for this app.
"""
from django.shortcuts import render
from django.views.generic import ListView

import platform
import django
from pytz import __version__ as pytz_version


class AboutList(ListView):
    context_object_name = 'about_list'

    def get_queryset(self, **kwargs):
        return [
                 {
                   'name'    : "Python",
                   'url'     : "http://www.python.org/",
                   'version' : platform.python_version(),
                 },
                 {
                   'name'    : "Django",
                   'url'     : "https://www.djangoproject.com/",
                   'version' : (str(django.VERSION[0]) + "." +
                                str(django.VERSION[1]) + "." +
                                str(django.VERSION[2])
                               ),
                 },
                 {
                   'name'    : "World Timezone Definitions for Python",
                   'url'     : "http://pytz.sourceforge.net/",
                   'version' : pytz_version,
                 }
               ]
