from django import forms
from .models import UserModel


choices = [('vendedor', 'vendedor'), ('cliente', 'cliente')]

class RegisterUser(forms.Form):
    imageuser = forms.ImageField()
    username  = forms.CharField(max_length=255)
    email     = forms.EmailField()
    password  = forms.CharField()
    status    = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    street    = forms.CharField(max_length=255)
    city      = forms.CharField(max_length=255)
    state     = forms.CharField(max_length=255)

    # description = forms.Textarea()


class FormLogin(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField()