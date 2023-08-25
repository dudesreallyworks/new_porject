from django.views.generic import ListView, DetailView, CreateView
from .models import News
from .filters import NewsFilter
from .forms import NewsForm


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'News'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'News'


class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'