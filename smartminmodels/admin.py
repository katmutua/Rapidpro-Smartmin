from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title']}),
                 ('Post information', {'fields': ['body', 'order', 'tags'], 'classes': ['collapse']})
                 ]


admin.site.register(Post)
