from django.contrib import admin
from django.urls import path, re_path
from users_register.views import *
from django.urls import reverse

app_name = 'users_register'

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('home/<str:user>/', index_page, name='index_page'),
    #path('home/<str:user>/post/<int:post_id>/', post_page, name='post_page'),
]

