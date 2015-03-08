"""Example Administration Module

This module contains the models which should be made available to the
administration interface.
"""
from django.contrib import admin
from exp.models import Stuff


admin.site.register(Stuff)
