from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Post, File, Comment


class FileInline(GenericTabularInline):
    model = File


class PostAdmin(admin.ModelAdmin):
    inlines = [FileInline]


class CommentAdmin(admin.ModelAdmin):
    inlines = [FileInline]


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(File)
