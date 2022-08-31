from django.db import models
from django.contrib.auth.models import AbstractUser

from .CustomManager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    mobile = models.CharField(max_length=11, unique=True)

    gender_choice = (
        ('female', 'خانم'),
        ('male', 'آقا')
    )

    image = models.ImageField('تصویر', default='account/static/images/profile_pictures/default.png',
                              upload_to="blog/static/images/profile_pictures",
                              blank=True, null=True)

    first_name = models.CharField('نام', max_length=50)
    last_name = models.CharField('نام خانوادگی', max_length=50)
    age = models.IntegerField('سن', null=True)
    gender = models.CharField('جنسیت', max_length=10, choices=gender_choice, null=True, blank=True)
    address = models.TextField(' آدرس', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    # code yebar masraf:
    # otp_code = models.PositiveIntegerField(blank=True, null=True)

    # time baraye expire shodan:
    # otp_created =models.DateTimeField(auto_now= True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile'

    REQUIRED_FIELDS = []

    backend = 'account.CustomBackend.ModelBackend'

