"""
	Configuration urls
"""

from .views import *

urlpatterns = PostCRUDL().as_urlpatterns()
