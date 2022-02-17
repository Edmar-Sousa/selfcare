from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts    import redirect
from ecommerce.form      import FormLogin, RegisterUser

from ecommerce.functions.user import registerLocalizationInModel, registerUserInModel, registerUserInUserDjangoModel


def validateFormLoginAndLoginUser(request):
    form = FormLogin(request.POST)

    if form.is_valid():
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)

        else:
            redirect('login')


def validateFormRegisterAndRegisterUser(request):
    form = RegisterUser(request.POST, request.FILES)

    if form.is_valid():
        userToRegistrad  = registerUserInUserDjangoModel(form)
        localizationUser = registerLocalizationInModel(form)
        registerUserInModel(form, userToRegistrad, localizationUser)

        redirect('login')

    else:
        redirect('register')