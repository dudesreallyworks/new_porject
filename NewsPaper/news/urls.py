from django.urls import path
from .views import NewsListView
from .views import NewsDetailView

urlpatterns = [path('news/', NewsListView.as_view(), name='news_post'),
               path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
               ]
