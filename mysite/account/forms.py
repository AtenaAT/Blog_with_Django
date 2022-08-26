# tanzime form registration ba vared kardan shomare mobile:
#---------------------------------------------------------------
from django import forms
from . import models
from blog.models import Profile

class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        
        fields = ['mobile', ]