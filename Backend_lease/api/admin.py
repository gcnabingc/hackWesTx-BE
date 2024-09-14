from django.contrib import admin
from . models import Usermodel
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


@admin.register(Usermodel)
class UsreModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password','confirmpassword']