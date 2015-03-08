"""Example Module

This module contains the views for this app.
"""
import time
import getpass
import textwrap
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.template import RequestContext

from exp.models import Stuff


def exp_view(request):
    from django.db import connection

    return render_to_response('exp/index.html')
