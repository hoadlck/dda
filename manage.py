"""Django Desktop Application Module

This module is the main routine for the Django project which is used as a
desktop application.
"""
import os
import sys

import http.cookies
import html.parser


module_name = "Django Desktop Application"
__version__ = "0.1"


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dda.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
