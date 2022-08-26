from django.contrib import admin
from .models import Comment,Post, Profile

# namayeshe model ha dar panel admin:
#________________________________________________________________
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post', 'created')
    search_fields = ('author', 'content')
#________________________________________________________________

@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_display= ('user','age','gender' )
    list_filter=('age','gender')
    search_fields= ('username',)
#________________________________________________________________
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('title','slug','published','status' )
    prepopulated_fields= {'slug':('title',)}
    list_filter=('published','status')
    search_fields= ('title','descripton')

