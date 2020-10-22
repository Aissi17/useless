from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta :
		model = User
		fields = ['username','email','password1','password2']

	# def __init__(self, *args, **kwargs):
	# 	super(CreateUserForm, self).__init__(*args, **kwargs)
	# 	self.fields['username'].widget.attrs['class'] = 'form-input'
	# 	self.fields['email'].widget.attrs['class'] = 'form-input'
	# 	self.fields['password1'].widget.attrs['class'] = 'form-control'
	# 	self.fields['password2'].widget.attrs['class'] = 'form-control'