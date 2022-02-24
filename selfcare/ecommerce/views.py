from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from .form   import RegisterUser, FormLogin, FormProduct
from .functions import auth

from .models import UserModel, LocalizationOfUser, ProductModel

from django.http import HttpResponse


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


def search(request):
    try:
        searchValue = request.GET['search']
        products = ProductModel.objects.filter(title__contains=searchValue)
    
    except:
        products = None

    return render(request=request, template_name='ecommerce/search-product.html', context={ 'products' : products })


@login_required
def profile(request, username):
    userDetails = UserModel.objects.filter(user__username=username).select_related('localization')
    productsUser = ProductModel.objects.filter(user=request.user)

    return render(
        request=request, 
        template_name='ecommerce/user-details.html', 
        context={ 'userDetails' : userDetails[0], 'products' : productsUser }
    )


@login_required
def addProduct(request):
    if request.method == 'POST':
        form = FormProduct(request.POST, request.FILES)

        if form.is_valid():
            productimage = form.cleaned_data['productimage']
            description  = form.cleaned_data['description']

            title = form.cleaned_data['title']
            price = form.cleaned_data['price']

            userLoggedIn = request.user

            productSaveInModel = ProductModel(
                user=userLoggedIn, 
                productImage=productimage, 
                description=description, 
                title=title, 
                price=price
            )
            productSaveInModel.save()

            form = FormProduct()
            return render(request=request, template_name='ecommerce/add-product.html', context={ 'form' : form, 'success' : True })

    else:
        form = FormProduct()
        return render(request=request, template_name='ecommerce/add-product.html', context={ 'form' : form })
