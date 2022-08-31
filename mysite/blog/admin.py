from django.contrib import admin
from .models import Comment, Post


# ________________________________________________________________
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post', 'created')
    search_fields = ('author', 'content')


# ________________________________________________________________


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'status')
    search_fields = ('title', 'description')
