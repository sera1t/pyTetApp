from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add state', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'LogIn', 'url_name': 'login'}
        ]

def index(request):
    user = users.objects.all()
    context = {
        'user': user,
        'menu': menu,
        'title': 'Home page'
    }
    return render(request, 'tetapp/index.html', context=context)

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('Contact Us')

def addpage(request):
    return HttpResponse('Add state')

def login(request):
    return HttpResponse('Log In')

def user(request, user_id):
    return HttpResponse(f"User in id ={user_id}")

def pageNotFound(request, exceprion):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')