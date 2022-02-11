from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^register/$', views.register, name='register')
]
