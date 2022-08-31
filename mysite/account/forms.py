from django import forms
from .models import CustomUser


class loginFrom(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("mobile",)


class RegisterFrom(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('mobile', "image", "first_name", "last_name", "age", "gender", "address")

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     CustomUser.objects.create()
    #     return user
