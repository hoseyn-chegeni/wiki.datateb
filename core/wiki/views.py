from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article

# Create your views here.
class IndexView(TemplateView):
    template_name= 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(is_published = True)
        return context