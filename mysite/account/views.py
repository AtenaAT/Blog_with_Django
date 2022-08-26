from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import CustomUser
from . import forms
from . import make_otp

#______________________________________________________________________________________________________
# register kardan va login ba otp

# def register_view(request):
#     form = forms.RegisterForm

#     if request.method == "POST":

#         try:
#             # ag user bashe:
#             if "mobile" in request.POST:
#                 mobile = request.POST.get('mobile')
#                 user = CustomUser.objects.get(mobile=mobile)
#                 # send otp
#                 otp = make_otp.get_random_otp()
#                 make_otp.send_otp(mobile, otp)
#                 # save otp
#                 # print(otp)
#                 user.otp = otp
#                 user.save()
#                 # tuye session zakhire beshe
#                 request.session['user_mobile'] = user.mobile
#                 return HttpResponseRedirect(reverse('verify'))

#         except CustomUser.DoesNotExist:
#             # ag user nabud:
#             form = forms.RegisterForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 # ag user bud hala otp barsh mifrestim
#                 # send otp
#                 otp = make_otp.get_random_otp()
#                 make_otp.send_otp(mobile, otp)
#                 # make_otp.send_otp_soap(mobile, otp)
#                 # save otp
#                 # print(otp)  # vase inke pul nare
#                 user.otp = otp
#                 user.is_active = False
#                 user.save()
#                 request.session['user_mobile'] = user.mobile
#                 return HttpResponseRedirect(reverse('verify'))

#     return render(request, 'register.html', {'form': form})
#______________________________________________________________________________________________________

def dashboard(request):
    return render(request, 'dashboard.html')

#______________________________________________________________________________________________________
#login bedune otp ba mobile:

def mobile_login(request):
    if request.method == "POST":
        if "mobile" in request.POST:
            mobile = request.POST.get('mobile')
            user = CustomUser.objects.get(mobile=mobile)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))

    return render(request, 'mobile_login.html')
#______________________________________________________________________________________________________
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
#             return HttpResponseRedirect(reverse('dashboard'))

#         return render(request, 'verify.html', {'mobile': mobile})
#     except:
#         return HttpResponseRedirect(reverse('register_view'))

