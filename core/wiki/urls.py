from django.urls import path
from .views import IndexView,ArticleDetailView
app_name = 'wiki'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail')
]