from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts    import redirect
from ecommerce.form      import FormLogin, RegisterUser

from ecommerce.functions.user import registerLocalizationInModel, registerUserInModel, registerUserInUserDjangoModel


def validateFormLoginAndLoginUser(request):
    form = FormLogin(request.POST)

    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('profile', username)

        else:
            return redirect('login')

    else:
        return redirect('login')


def validateFormRegisterAndRegisterUser(request):
    form = RegisterUser(request.POST, request.FILES)

    if form.is_valid():
        userToRegistrad  = registerUserInUserDjangoModel(form)
        localizationUser = registerLocalizationInModel(form)
        registerUserInModel(form, userToRegistrad, localizationUser)

        redirect('login')

    else:
        redirect('register')