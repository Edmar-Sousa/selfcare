from django.contrib.auth.models import User
from ecommerce.models import UserModel, LocalizationOfUser


def registerUserInUserDjangoModel(form):
    nameUserToRegister  = form.cleaned_data['username']
    emailUserToRegister = form.cleaned_data['email']
    passwordUserToRegister = form.cleaned_data['password']

    userToRegistrad = User.objects.create_user(nameUserToRegister, emailUserToRegister, passwordUserToRegister)
    userToRegistrad.save()

    return userToRegistrad


def registerLocalizationInModel(form):
    street = form.cleaned_data['street']
    city   = form.cleaned_data['city']
    state  = form.cleaned_data['state']
    localizationUser = LocalizationOfUser(street=street, city=city, state=state)
    localizationUser.save()

    return localizationUser


def registerUserInModel(form, userToRegistrad, localizationUser):
    userImage = form.cleaned_data['imageuser']
    status = form.cleaned_data['status']

    userRegistrad = UserModel(user=userToRegistrad, userImage=userImage, status=status, localization=localizationUser)
    userRegistrad.save()