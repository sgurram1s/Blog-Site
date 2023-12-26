from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PostData


def register_page(request):
    if request.user.is_authenticated:
        user = request.user
        return redirect('users_register:index_page', user)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_register:login_page')
        else:
            return render(request, 'users_register/register_page.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'users_register/register_page.html', {'form': form})


def login_page(request):   
    if request.user.is_authenticated:
        user = request.user
        return redirect('users_register:index_page', user)
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            #user = authenticate(request, username = user_data.username, password = user_data.password)
            if user is not None:
                login(request, user)
                user = request.user
                #user_path = user.first_name.replace(" ","")                
                #print(user_path)
                return redirect('users_register:index_page',user)
            else:
                return HttpResponse('Invalid Credentials')
        else:
            return render(request, 'users_register/login_page.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'users_register/login_page.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect("initial_page")


@login_required(login_url='users_register:login_page')
def index_page(request, **kwargs):
    user_name = kwargs['user']
    user = User.objects.get(username=user_name)
    user_name = user.first_name
    
    data = PostData.objects.all().order_by('-date_posted')
        
    content ={
        'user_name': user_name,
        'data': data,
    }
    
    return render(request, "users_register/index_page.html", content)


def post_page(request, **kwargs):
    post__id = kwargs['post_id']
    data = PostData.objects.get(id=post__id)
    
    content ={
        data: data,
    }
    
    return render(request, "users_register/post_page.html", content)

