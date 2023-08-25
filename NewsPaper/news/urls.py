from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreate

urlpatterns = [path('', NewsListView.as_view(), name='news_list'),
               path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
               path('create/', NewsCreate.as_view(), name='news_create'),
               ]
