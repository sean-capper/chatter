from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name="login"),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name="logout")
]