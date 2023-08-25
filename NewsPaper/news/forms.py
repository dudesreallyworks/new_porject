from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'post_type',
            'author',
            'title',
            'text',
            'content',
        ]
