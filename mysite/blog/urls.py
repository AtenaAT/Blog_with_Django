from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [

    path('<slug:slug>/', views.post_details, name='post_details'),
    path('', views.posts_list, name='posts_list'),
    # path('posts/like/', views.like_post, name='like_post'),


] + staticfiles_urlpatterns()
