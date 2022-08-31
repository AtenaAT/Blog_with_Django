from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import CustomUser as User
from . import forms
from . import make_otp
from blog.views import posts_list


# ______________________________________________________________________________________________________

# login bedune otp ba mobile:

def custom_login(request):
    form = forms.loginFrom
    if request.method == "POST":
        if "mobile" in request.POST:
            mobile = request.POST.get('mobile')
            user = User.objects.get(mobile=mobile)
            login(request, user)
            return HttpResponseRedirect(reverse(posts_list))

    return render(request, 'login.html', {'form': form})


# ______________________________________________________________________________________________________
def custom_register(request):
    if request.method == "POST":
        form = forms.RegisterFrom(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()

            user = form.save(commit=True)
            User.objects.create()
            user.save()
            form.save()
            login(request, user)
            return HttpResponseRedirect(reverse(posts_list))
    form = forms.RegisterFrom()
    return render(request, 'register.html', {'form': form})


# ______________________________________________________________________________________________________
def custom_logout(request):
    logout(request)
    return render(request, "logout.html")


# ______________________________________________________________________________________________________

@login_required
def profile_detail(request):
    profile = request.user
    return render(request, "profile.html", {"profile": profile})
# ______________________________________________________________________________________________________
# register kardan va login ba otp

# def register_view(request):
#     form = forms.LoginFrom

#     if request.method == "POST":

#         try:
#             # ag user bashe:
#             if "mobile" in request.POST:
#                 mobile = request.POST.get('mobile')
#                 user = CustomUser.objects.get(mobile=mobile)
#
#                 otp = make_otp.get_random_otp()
#                 make_otp.send_otp(mobile, otp)
#
#                 print(otp)
#                 user.otp = otp
#                 user.save()
#                 # tuye session zakhire beshe
#                 request.session['user_mobile'] = user.mobile
#                 return HttpResponseRedirect(reverse('verify'))

#         except CustomUser.DoesNotExist:
#             # ag user nabud:
#             form = forms.LoginFrom(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 # ag user bud hala otp barsh mifrestim
#
#                 otp = make_otp.get_random_otp()
#                 make_otp.send_otp(mobile, otp)

#                 user.otp = otp
#                 user.is_active = False
#                 user.save()
#                 request.session['user_mobile'] = user.mobile
#                 return HttpResponseRedirect(reverse('verify'))

#     return render(request, 'register.html', {'form': form})
# ______________________________________________________________________________________________________
# verify kardan user ba otp:

# def verify(request):
#     try:
#         mobile = request.session.get('user_mobile')
#         user = CustomUser.objects.get(mobile=mobile)
#         if request.method == "POST":

#             if user.otp != int(request.POST.get('otp')):
#                  return HttpResponseRedirect(reverse('verify'))

#             user.is_active = True
#             user.save()
#             login(request, user)
#             return HttpResponseRedirect(reverse(posts-list))

#         return render(request, 'verify.html', {'mobile': mobile})
#     except:
#         return HttpResponseRedirect(reverse('register'))

# _____________________________________________________________________________________________________
