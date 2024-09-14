from django.shortcuts import render
from .serializers import UserData_Serializers
# ,UserData_Serializers
from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import Usermodel
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json


from django.contrib.auth import login,logout,authenticate

from django.http import HttpResponse

def home(request):
    return HttpResponse("This is a home page")

class Property_list(ListAPIView):
    queryset=Usermodel.objects.all()
    serializer_class=UserData_Serializers
    
@csrf_exempt
def create_user_account(request):
    
    if request.method == 'POST':
        try:    
            data=request.body.decode('utf-8')
            user_data = json.loads(data)
            print(user_data)
            signup_data = user_data.get('values')
            print(signup_data)
            if signup_data:
                name = signup_data.get('name')
                email = signup_data.get('email').lower()
                password = signup_data.get('password')
                # if User.objects.filter(email=email).exists():
                #      return JsonResponse({'error': 'Email address already in use'}, status=401)
                # else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()           
                    # return JsonResponse({'message': 'User created successfully'}, status=201)
            return JsonResponse({'message': 'User not found'}, status=400)
        except IntegrityError:
                return JsonResponse({'error': 'Username already exists'}, status=402)

    return JsonResponse({'message': 'data not received'}, status=404)



@csrf_exempt
def login_user(request):
    pass
    if request.method == 'POST':
        try:
            data=request.body.decode('utf-8')
            user_data = json.loads(data)
            Login_data = user_data.get('Login_data')
            if Login_data:
                name = Login_data.get('name').lower()
                password =Login_data.get('password')
                print(name,password)
                user = authenticate(username=name, password=password)
                if user is not None:
                         login(request,user)
                         return JsonResponse({'message': 'User login successfully'}, status=201)
                else:
                    print("user is none")
               
            return JsonResponse({"message":"no logindata "},status=400)
        except:
            return JsonResponse({'error': 'Error in fetching data'}, status=401)
    return JsonResponse({'error': 'request method is not POST request'}, status=410)