from django.db import models
from django.contrib.auth.models import User


# class LocalizationOfUser(models.Model):
#     street = models.CharField(max_length=255)
#     city   = models.CharField(max_length=255)
#     state  = models.CharField(max_length=2) # XY


# class UserModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     userImage = models.FileField(upload_to='/upload', max_length=255)

#     status = models.CharField(max_length=255)
#     localization = models.ForeignKey(LocalizationOfUser, on_delete=models.CASCADE)

#     description = models.CharField(max_length=255)
