from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import home
from market import settings
from user.views import basket, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('basket/', basket, name='basket'),
    path('add_item/', home, name='add_item'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]