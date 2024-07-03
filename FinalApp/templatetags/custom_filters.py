from django import template
import os

register = template.Library()

def filename_from_path(value):
    return os.path.basename(value)

register.filter('filename_from_path', filename_from_path)
