from django.shortcuts import render
from django.http import HttpResponse

def initial_page(request):
    return render(request, 'openspeech/initial_page.html')