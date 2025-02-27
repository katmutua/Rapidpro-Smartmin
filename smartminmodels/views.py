from smartmin.views import *
from .models import *
from django import forms
from django.contrib.auth.models import User


class ExcludeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'order', 'tags')


class CategoryForm(forms.ModelForm):
    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Category
        fields = ('name',)


class UserCRUDL(SmartCRUDL):
    model = User
    permissions = False
    actions = ('list',)


class CategoryCRUDL(SmartCRUDL):
    model = Category

    class Create(SmartCreateView):
        form_class = CategoryForm


class PostCRUDL(SmartCRUDL):
    model = Post
    actions = ('create', 'read', 'update', 'delete', 'list', 'author',
               'exclude', 'exclude2', 'readonly', 'readonly2', 'messages', 'csv_import')

    class List(SmartListView):
        fields = ('title', 'tags', 'created_on', 'created_by')
        search_fields = ('title__icontains', 'body__icontains')
        default_order = 'title'

        def as_json(self, context):
            items = []
            for obj in self.object_list:
                items.append(dict(title=obj.title,
                                  body=obj.body,
                                  tags=obj.tags))

            return items

    class Author(SmartListView):
        fields = ('title', 'tags', 'created_on', 'created_by')
        default_order = ('created_by__username', 'order')

    class Update(SmartUpdateView):
        success_message = "Your blog post has been updated."

    class Create(SmartCreateView):
        submit_button_name = "Create New Post"

    class Exclude(SmartUpdateView):
        exclude = ('tags',)

    class Exclude2(SmartUpdateView):
        form_class = ExcludeForm
        exclude = ('tags',)

    class Readonly(SmartUpdateView):
        readonly = ('tags',)

    class Readonly2(SmartUpdateView):
        form_class = ExcludeForm
        readonly = ('tags',)

    class Messages(SmartListView):
        def pre_process(self, request, *args, **kwargs):
            messages.error(request, "Error Messages")
            messages.success(request, "Success Messages")
            messages.info(request, "Info Messages")
            messages.warning(request, "Warning Messages")
            messages.debug(request, "Debug Messages")
