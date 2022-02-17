from django.shortcuts import render, redirect

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


from .form   import RegisterUser, FormLogin
from .functions import auth

def index(request):
    return render(request=request, template_name='ecommerce/index.html')


def login(request):
    if request.method == 'POST':
        auth.validateFormLoginAndLoginUser(request)

    else:
        form = FormLogin()
        return render(request=request, template_name='ecommerce/login.html', context={ 'form' : form })


def logout(request):
    auth_logout(request)
    return redirect('register')


def register(request):
    if request.method == 'POST':
        auth.validateFormRegisterAndRegisterUser(request)
        return render(request=request, template_name='ecommerce/register-success.html')

    else:
        form = RegisterUser()
        return render(request=request, template_name='ecommerce/register.html',  context={ 'form' : form })


@login_required
def profile(request, username):
    return render(request=request, template_name='ecommerce/user-details.html')

