from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponse

def index(request):
    return render(request=request, template_name='ecommerce/index.html')


def login(request):
    return render(request=request, template_name='ecommerce/login.html')


def register(request):

    if request.method == 'POST':
        userName = request.POST['username']
        email    = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(userName, email, password)
        user.save()

        return render(
            request=request, 
            template_name='ecommerce/register-success.html', 
            context={ 'username' : userName })

    else:
        return render(request=request, template_name='ecommerce/register.html')
    