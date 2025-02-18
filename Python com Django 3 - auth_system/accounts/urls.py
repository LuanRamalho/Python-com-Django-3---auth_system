from django.urls import path
from .views import register, user_login, user_logout, auth_home

urlpatterns = [
    path('', auth_home, name='auth_home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
