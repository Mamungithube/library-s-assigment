from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Comment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ChangeuserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']