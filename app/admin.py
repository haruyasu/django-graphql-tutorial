from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post

class PostCustom(ModelAdmin):
    list_display = ("channel_name", "caption", "created_at")
    list_display_links = ("channel_name",)
    ordering = ("-created_at",)

admin.site.register(Post, PostCustom)
