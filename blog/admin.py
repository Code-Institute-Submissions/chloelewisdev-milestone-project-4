from django.contrib import admin
from .models import OwnerBlog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'blog_title',
        'blog_content',
        'date_added',
    )

    ordering = ('date_added',)


admin.site.register(OwnerBlog, BlogAdmin)
