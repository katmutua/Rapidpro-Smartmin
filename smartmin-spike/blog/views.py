from smartmin.views import *
from .models import *

class PostCRUDL(SmartCRUDL):
    actions = ('create', 'update', 'list')
    model = Post
