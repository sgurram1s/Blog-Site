from django.contrib import admin
from django.urls import path, include
from openspeech.views import initial_page


app_name = 'openspeech'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initial_page, name='initial_page'),
    
    # registering the urls from users_register app
    path('', include('users_register.urls')),
]