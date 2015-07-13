from smartmin.views import *
from .models import *
from django import forms
from django.contrib.auth.models import User

# class UserCRUDL(SmartCRUDL):
#     model = User
#     permissions = False
#     actions = ('list',)

class PostCRUDL(SmartCRUDL):
    model = Post
    actions = ('create', 'read', 'update', 'delete', 'list')