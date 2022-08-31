from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class MobileBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # mobile az kwargs begire: 
        mobile = kwargs['mobile']
        try:
            user = CustomUser.objects.get(mobile=mobile)
            
        except CustomUser.DoesNotExist:
            pass

