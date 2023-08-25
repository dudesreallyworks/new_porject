from django_filters import FilterSet
from .models import News
from .models import Category


class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = {
            'title': ['icontains'],
        }