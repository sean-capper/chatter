from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ChatterUserCreationForm, ChatterUserChangeForm

# Create your views here
def index(request):
    if request.user.is_authenticated:
        return redirect('chatter:index')
    return render(request, 'index.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('chatter:index')
    elif request.POST:
        form = ChatterUserCreationForm(request.POST)
        if(form.is_valid):
            user = form.save()
            login(request, user)
            return redirect('accounts:index')
    else:
        form = ChatterUserCreationForm()

    return render(request, 'signup.html', {
        'form': form,
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('chatter:index')
    elif request.POST:
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('chatter:index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {
        'form': form,
    })

def logout_view(request):
    if request.POST:
        logout(request)
        return redirect('accounts:index') 