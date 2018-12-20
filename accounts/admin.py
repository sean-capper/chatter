from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ChatterUserCreationForm, ChatterUserChangeForm
from .models import User

class ChatterUserAdmin(UserAdmin):
    add_form = ChatterUserCreationForm
    form = ChatterUserChangeForm
    model = User
    list_display = ['user_id', 'username',]

admin.site.register(User, ChatterUserAdmin)