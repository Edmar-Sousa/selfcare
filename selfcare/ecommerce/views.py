from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from .form   import RegisterUser, FormLogin
from .functions import auth

from .models import UserModel, LocalizationOfUser


def index(request):
    return render(request=request, template_name='ecommerce/index.html')


def login(request):
    if request.method == 'POST':
        return auth.validateFormLoginAndLoginUser(request)

    else:
        form = FormLogin()
        return render(request=request, template_name='ecommerce/login.html', context={ 'form' : form })


def logout(request):
    auth_logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        auth.validateFormRegisterAndRegisterUser(request)
        return render(request=request, template_name='ecommerce/register-success.html')

    else:
        form = RegisterUser()
        return render(request=request, template_name='ecommerce/register.html',  context={ 'form' : form })


@login_required
def profile(request, username):
    userDetails = UserModel.objects.filter(user__username=username).select_related('localization')
    return render(request=request, template_name='ecommerce/user-details.html', context={ 'userDetails' : userDetails[0] })

