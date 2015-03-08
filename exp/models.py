"""Example Models Module

This module contains the class which define the database schema for
storing information about Example things.
"""
from django.db import models


class Stuff(models.Model):
    """Stuff Table"""

    #Name
    #     This is the stuff's name.
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)
