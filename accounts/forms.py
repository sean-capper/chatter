from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class ChatterUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username',)

class ChatterUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'password')