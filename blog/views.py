from django.shortcuts import render
from django.views import generic
from .forms.indexform import ArticleForm
# Create your views here.


class IndexView(generic.FormView):
    template_name = 'blog/index.html'
    form_class = ArticleForm
    initial = {'title':'I \'m title.',
        'content':'This is the article ,please write here.',
        'author':'janes',
        'pub_date':'2011-11-25 13:23:08'}
    success_url='/blog/'
