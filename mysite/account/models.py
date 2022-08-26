# tarif model custom user
# -----------------------------

from django.db import models
from django.contrib.auth.models import AbstractUser

from .CustomManager import CustomUserManager

class CustomUser(AbstractUser):

    username = None
    mobile = models.CharField(max_length=11, unique= True)

    #code yebar masraf:
    # otp_code = models.PositiveIntegerField(blank=True, null=True)

    # time baraye expire shodan:
    # otp_created =models.DateTimeField(auto_now= True)

    objects= CustomUserManager()

    USERNAME_FIELD= 'mobile'

    REQUIRED_FIELDS =[]

    backend= 'account.CustomBackend.ModelBackend'

-----------------------------------------
