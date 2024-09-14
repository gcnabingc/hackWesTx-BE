from django.contrib.auth.backends import BaseBackend
from .models import Usermodel

class CustomUserModelBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Usermodel.objects.get(email=email)
            if user.check_password(password):
                return user
        except Usermodel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usermodel.objects.get(pk=user_id)
        except Usermodel.DoesNotExist:
            return None