from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name= 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(is_published = True)
        return context
    
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name =  'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(is_published = True)
        return context