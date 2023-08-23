from django.views.generic import ListView
from django.views.generic import DetailView
from .models import News


class NewsListView(ListView):
    model = News
    ordering = 'created_at'
    template_name = 'news_list.html'
    context_object_name = 'news_post'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news_post'
