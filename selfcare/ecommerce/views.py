from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponse

from .form   import RegisterUser
from .models import UserModel, LocalizationOfUser

from .functions.user import registerLocalizationInModel, registerUserInModel, registerUserInUserDjangoModel

def index(request):
    return render(request=request, template_name='ecommerce/index.html')


def login(request):
    return render(request=request, template_name='ecommerce/login.html')


def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST, request.FILES)

        if form.is_valid():
            userToRegistrad  = registerUserInUserDjangoModel(form)
            localizationUser = registerLocalizationInModel(form)
            registerUserInModel(form, userToRegistrad, localizationUser)

            return render(
                request=request, 
                template_name='ecommerce/register-success.html')

    else:
        form = RegisterUser()
        return render(request=request, template_name='ecommerce/register.html',  context={ 'form' : form })
    

def profile(request, username):
    return render(request=request, template_name='ecommerce/user-details.html')


def finish(request):
    return render(request, template_name='ecommerce/complete-register.html')