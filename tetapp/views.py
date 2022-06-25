from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add state', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'LogIn', 'url_name': 'login'}
        ]

def index(request):
    post = posts.objects.all()

    context = {
        'posts': post,
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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                posts.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Error add state')
    else:
        form = AddPostForm()
    return render(request, 'tetapp/addpage.html', {'form': form, 'menu': menu, 'title': 'Add state'})

def login(request):
    return HttpResponse('Log In')

def show_posts(request, post_id):
    post = get_object_or_404(posts, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'tetapp/post.html', context=context)

def show_category(request, cat_id):
    post = posts.objects.filter(cat_id=cat_id)

    if len(post) == 0:
        raise Http404()

    context = {
        'posts': post,
        'menu': menu,
        'title': 'Category stage',
        'cat_selected': cat_id,
    }
    return render(request, 'tetapp/index.html', context=context)

def pageNotFound(request, exceprion):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
