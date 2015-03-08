"""Example URL Module

This module contains the rule mapping for the various URLs associated with
this app.
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from exp.views import exp_view


urlpatterns = patterns(
    '',
    url(r'^$', exp_view, name='exp_view'),
)
