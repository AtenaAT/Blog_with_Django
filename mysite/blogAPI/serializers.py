from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from account.models import CustomUser as User
from blog.models import Post, Comment
import re


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# ---------------------------------------------------------------------------------------------------
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.mobile')
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'description', 'created', 'status', 'image', 'comments']


# ---------------------------------------------------------------------------------------------------
class UserListSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    author_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # author_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'posts', 'is_staff', 'is_active', 'mobile', 'first_name', 'last_name', 'age',
                  'gender', 'author_comments']


# ---------------------------------------------------------------------------------------------------
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile', 'first_name', 'last_name', 'age', 'gender', 'address']

    def validate_mobile(self, value):
        mobile = re.compile("^09\d{9}$")
        if mobile.match(value):
            return value
        raise ValidationError("mobile error")
