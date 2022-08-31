from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .filters import OrderFilter
from .models import Post, Comment, Like
from .forms import CommentForm
from account.models import CustomUser as User


# all post

def posts_list(request):
    post_list = Post.objects.all()

    my_filter = OrderFilter(request.GET, queryset=post_list)
    post_list = my_filter.qs

    context = {
        'post_list': post_list,
        'my_filter': my_filter,
    }

    return render(request, "posts_list.html", context)


# ______________________________________________________________________________________________________
# post details & comments:

def post_details(request, slug):
    template_name = 'post_details.html'
    profile_list = User.objects.all()
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    new_comment = None

    if request.method == 'POST':

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            # object jadid:

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            comment_form.save()
            new_comment.save()
            return redirect('.')
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post, 'comments': comments,
                                           'comment_form': comment_form})


# ________________________________________________________________________________________________________
# like

# @login_required
# def like_post(request):
#     author = request.user
#     if request.method == 'POST':
#         # like_form = LikeForm(request.POST)
#         post_id = request.POST.get(Post.id)
#         post_object = Post.objects.get(id=post_id)
#         # post_object = Post.objects.get(id=post_id)
#     if author in post_object.likes.all():
#         post_object.like.remove(author)
#     else:
#         post_object.like.add(author)
#         like, created = Like.objects.get_or_create(author=author, post_id=post_id)
#
#         if not created:
#             if like.value == 'Like':
#                 like.value = 'Unlike'
#             else:
#                 like.value = 'Like'
#                 like.save()
#
#     return redirect(post_details, slug=Post.slug)
# _______________________________________________________________________________________
