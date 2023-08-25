from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        articles_rating = self.post_set.aggregate(Sum('rating'))[
                              'rating__sum'] * 3  # вычисляется суммарный рейтинг всех статей автора, который затем умножается на 3.
        comments_rating = self.comment_set.aggregate(Sum('rating'))[
            'rating__sum']  # вычисляется суммарный рейтинг всех комментариев автора.
        articles_comments_rating = \
            self.post_set.annotate(  # вычисляется суммарный рейтинг всех комментариев к статьям автора.
                comments_rating=Sum('comment__rating')
            ).aggregate(Sum('comments_rating'))['comments_rating__sum']

        self.rating = articles_rating + comments_rating + articles_comments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name.title()


class News(models.Model):
    ARTICLE = 'article'
    NEWS = 'news'
    POST_TYPES = (
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    rating = models.IntegerField(default=0)
    content = models.TextField()

    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def preview(self):
        preview_length = 124
        if len(self.content) <= preview_length:
            return self.content
        else:
            return self.content[:preview_length] + "..."

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.post.title} - Category: {self.category.name}"


class Comment(models.Model):
    post = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.text
    # Здесь мы добавляем две связи «один ко многим» - с моделью Post и со встроенной моделью User.
    # С помощью ForeignKey указываем, что каждый комментарий принадлежит определенному посту и определенному пользователю.
    # Поле "text" будет содержать текст комментария.
    # Поле "creation_date" будет содержать дату и время создания комментария. Устанавливаем значение auto_now_add=True, чтобы автоматически заполнять это поле текущим временем при создании объекта.
    # Поле "rating" будет содержать рейтинг комментария (например, количество лайков или дизлайков).
    # Таким образом, модель Comment позволяет хранить информацию о комментариях к новостям или статьям, а также связывать эти комментарии с соответствующими постами и пользователями.
