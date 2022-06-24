from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add state', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'LogIn', 'url_name': 'login'}
        ]

def index(request):
    post = posts.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': post,
        'cats': cats,
        'menu': menu,
        'title': 'Home page',
        'cat_selected': 0,
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

def show_posts(request, post_id):
    return HttpResponse(f"Post in id ={post_id}")

def show_category(request, cat_id):
    post = posts.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(post) == 0:
        raise Http404()

    context = {
        'posts': post,
        'cats': cats,
        'menu': menu,
        'title': 'Category stage',
        'cat_selected': cat_id,
    }
    return render(request, 'tetapp/index.html', context=context)

def pageNotFound(request, exceprion):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')