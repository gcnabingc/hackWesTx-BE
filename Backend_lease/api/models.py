from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



class Usermodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password =models.CharField(max_length=100)
    confirmpassword =models.CharField(max_length=100)    
    
    def __str__(self):
        return self.email
   