from django import forms
from .models import Comment,Post,Profile
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser as User

#____________________________________________________________________________________________________
# form comment baraye user:

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'content')

#____________________________________________________________________________________________________
# form registration baraye user:

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model =  User
		
		# fields = ( "image", "first_name", "last_name","age","gender","address")

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	if commit:
	# 		user.save()
	# 	return user
#____________________________________________________________________________________________________

class Profile():
	pass
#____________________________________________________________________________________________________

