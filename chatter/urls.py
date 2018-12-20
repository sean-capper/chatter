from django.urls import path

from chatter import views

app_name = 'chatter'

urlpatterns = [
    path('', views.index, name='index'),
]