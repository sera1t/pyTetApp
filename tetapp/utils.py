from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add state', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'LogIn', 'url_name': 'login'}
]

class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                cats = Category.objects.all()
                context['menu'] = menu
                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context