from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request=request, template_name='ecommerce/index.html')


def login(request):
    return render(request=request, template_name='ecommerce/login.html')


def register(request):
    return render(request=request, template_name='ecommerce/register.html')