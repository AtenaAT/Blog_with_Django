from django.contrib import messages
from django.contrib.auth import login, logout , authenticate
from account.models import CustomUser as User
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .filters import OrderFilter
from .models import Post,Comment,Like, Profile
from .forms import CommentForm, NewUserForm

#______________________________________________________________________________________________________
#profile


#______________________________________________________________________________________________________
# baraye registration

def register_request(request):

	if request.method == "POST":

		form = NewUserForm(request.POST)
		if form.is_valid():

			user = form.save()
			login(request, user)
			return HttpResponseRedirect(reverse('posts_list'))
		
	form = NewUserForm()
	return render (request, template_name="register.html", context={"register_form":form})
#_______________________________________________________________________________________________________
#login 

def login_request(request):

	if request.method == "POST":

		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:

				login(request, user)
				return HttpResponseRedirect(reverse('posts_list'))

	form = AuthenticationForm()
	return render(request, template_name="login.html", context={"login_form":form})
#_______________________________________________________________________________________________________
# logout

def custom_logout(request):

    logout(request)
    return render (request=request, template_name="logout.html")
#_______________________________________________________________________________________________________

# class profile_detail(ListView):
#     model = Profile
#     template_name = "profile.html"
#     fields = ['user','image','first_name','last_name','age','gender','address',]
@login_required
def profile_detail(request):
    profile = request.user.profile
    
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)
#______________________________________________________________________________________________________
# all post

def posts_list(request):

    post_list= Post.objects.all()

    # baraye django filter:
    my_filter = OrderFilter(request.GET, queryset= post_list)
    post_list = my_filter.qs
    
    context={
        'post_list':post_list,
        'my_filter':my_filter,
    }

    return render(request,"posts_list.html", context)

#______________________________________________________________________________________________________
# post detals & comments:

def post_details(request, slug):

    template_name = 'post_details.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    new_comment = None

    # Comment posted
    if request.method == 'POST' and  Comment.author.is_authenticated():

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            # object jadid: 
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,'comments': comments,'new_comment': new_comment
                                           ,'comment_form': comment_form})
#________________________________________________________________________________________________________
#like

@login_required
def like_post(request):
    
    author = request.user
    if request.method == 'POST':
        # like_form = LikeForm(request.POST)
        post_id = request.POST.get(Post.id)
        post_object =Post.objects.get(id=post_id)
        #post_object = Post.objects.get(id=post_id)
    if author in post_object.likes.all():
        post_object.like.remove(author)
    else:
        post_object.like.add(author)
        like, created = Like.objects.get_or_create(author=author,post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
                like.save()

    return redirect(post_details, slug=Post.slug)
#_______________________________________________________________________________________

# def post_new(request):

#     if request.method == "POST":

#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():

#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
#_______________________________________________________________________________________

# def post_edit(request, pk):

#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":

#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():

#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
