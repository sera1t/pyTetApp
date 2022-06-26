from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import *
from .models import *
from .utils import *

class TetHome(DataMixin, ListView):
    model = posts
    template_name = 'tetapp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home page')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return posts.objects.filter(is_published=True)

# def index(request):
#     post = posts.objects.all()
#
#     context = {
#         'posts': post,
#         'menu': menu,
#         'title': 'Home page',
#         'cat_selected': 0,
#     }
#     return render(request, 'tetapp/index.html', context=context)

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('Contact Us')

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'tetapp/addpage.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add state')
        return dict(list(context.items()) + list(c_def.items()))

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'tetapp/addpage.html', {'form': form, 'menu': menu, 'title': 'Add state'})

def login(request):
    return HttpResponse('Log In')

# def show_posts(request, post_id):
#     post = get_object_or_404(posts, pk=post_id)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'tetapp/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = posts
    template_name = 'tetapp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add state')
        return dict(list(context.items()) + list(c_def.items()))

class TetCategory(DataMixin, ListView):
    model = posts
    template_name = 'tetapp/index.html'
    slug_url_kwarg = 'cat_slug'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return posts.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(request, cat_id):
#     post = posts.objects.filter(cat_id=cat_id)
#
#     if len(post) == 0:
#         raise Http404()
#
#     context = {
#         'posts': post,
#         'menu': menu,
#         'title': 'Category stage',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'tetapp/index.html', context=context)

def pageNotFound(request, exceprion):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
