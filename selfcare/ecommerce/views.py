from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from .form   import RegisterUser, FormLogin, FormProduct
from .functions import auth, product

from .models import UserModel, LocalizationOfUser, ProductModel


def index(request):
    products = ProductModel.objects.all()[:6]
    return render(request=request, template_name='ecommerce/index.html', context={ 'products' : products })


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


def productDetails(request, productId):
    product = ProductModel.objects.filter(id=productId)[0]
    return render(request=request, template_name='ecommerce/details.html', context={ 'product' : product })


@login_required
def profile(request, username):
    userDetails = UserModel.objects.filter(user__username=username).select_related('localization')
    productsUser = ProductModel.objects.filter(user=request.user)

    return render(
        request=request, 
        template_name='ecommerce/user-details.html', 
        context={ 'userDetails' : userDetails[0], 'products' : productsUser })


@login_required
def addProduct(request):
    if request.method == 'POST':
        response = product.addProductInDatabase(request)
        context = { }

        if (response['is_valid']):
            form = FormProduct()

        else:
            form = response['form_data']

        context['form'] = form
        context['msg']  = response['msg']
        return render(request=request, template_name='ecommerce/add-product.html', context=context)

    else:
        form = FormProduct()
        return render(request=request, template_name='ecommerce/add-product.html', context={ 'form' : form })
