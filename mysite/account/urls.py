from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('verify/', views.verify, name='verify'),
    path('register/', views.custom_register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path("profile/", views.profile_detail, name='profile_detail'),

]
urlpatterns += staticfiles_urlpatterns()
