
from django.urls import path
from api import views
# from .views import create_user

urlpatterns = [
    path('', views.home),
    path('users/',views.Property_list.as_view()),
    path('create_user_account/', views.create_user_account, name='create_user_account'),
    path('login_user/', views.login_user, name='login_user'),
]