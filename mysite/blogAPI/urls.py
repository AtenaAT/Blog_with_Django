from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, PostListAPIView, PostDetailAPIView, \
    CommentListAPIView, CommentDetailAPIView, UserCreateAPIView

urlpatterns = [

    path('user/<int:id>/', UserDetailAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('user/new/', UserCreateAPIView.as_view()),
    # _______________________________________________________
    path('posts/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),
    path('comments/', CommentListAPIView.as_view()),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view()),
]
