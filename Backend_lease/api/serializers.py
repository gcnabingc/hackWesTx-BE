from rest_framework import serializers
from .models import Usermodel

class UserData_Serializers(serializers.ModelSerializer):
        class Meta:
            model =Usermodel
            fields = ['id','name','email']