"""Django Desktop Application URL Module

This module contains the rule mapping for the various URLs associated with
this project.
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from dda.views import AboutList


urlpatterns = patterns(
    '',

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),

    url(r'^exp/',   include('exp.urls')),

    url(r'^about/',  AboutList.as_view(template_name="about.html")),

    url(r'^admin/',  include(admin.site.urls)),
)
