from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns =[
    path("profile/",views.profile_detail, name='profile_detail'),
    path('<slug:slug>/', views.post_details, name='post_details'),
    path('', views.posts_list, name='posts_list'),
    path('posts/like/',views.like_post, name='like_post'),

    #users url
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("log-out", views.custom_logout, name='logout'),   
]

urlpatterns += staticfiles_urlpatterns()