"""
	Configuration urls
"""

from django.conf.urls import include, patterns, url
from .views import *

urlpatterns = PostCRUDL().as_urlpatterns()

