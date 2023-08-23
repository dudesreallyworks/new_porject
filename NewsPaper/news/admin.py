from django.contrib import admin
from .models import News
from .models import Author
from .models import Category
from .models import PostCategory
from .models import Comment

admin.site.register(News)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
